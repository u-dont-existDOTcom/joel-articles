"""Reuse exact completed requests; never resample an interrupted reserved call."""
import hashlib
import json
import os


def key(identifier, phase, prompt):
    return (identifier, phase, hashlib.sha256(prompt.encode()).hexdigest())


def complete_lines(path):
    if not path.exists():
        return []
    raw = path.read_bytes()
    assert not raw or raw.endswith(b'\n'), f'Incomplete journal tail: preserve and reconcile {path.name} before resuming'
    return [json.loads(line) for line in raw.split(b'\n')[:-1] if line]


class RequestCache:
    def __init__(self, requests, reservations):
        self.reservations = reservations
        self.completed = {}
        for row in complete_lines(requests):
            assert len(row['messages']) == 1 and row['messages'][0]['role'] == 'user'
            identity = key(row['id'], row['phase'], row['messages'][0]['content'])
            answer = {'text': row['response'], 'truncated': row['truncated'],
                      'request': row['request']}
            if identity in self.completed:
                previous = self.completed[identity]
                assert previous['text'] == answer['text'] and previous['truncated'] == answer['truncated'], 'Conflicting exact request outputs require reconciliation'
            else:
                self.completed[identity] = answer
        self.reserved = {tuple(row['key']) for row in complete_lines(reservations)}

    def lookup(self, identifier, phase, prompt):
        identity = key(identifier, phase, prompt)
        if identity in self.completed:
            return self.completed[identity]
        if identity in self.reserved:
            raise RuntimeError(f'Unrecovered reserved request {identifier}/{phase}; do not resample. Preserve and reconcile the interrupted call.')
        return None

    def reserve(self, identifier, phase, prompt):
        identity = key(identifier, phase, prompt)
        assert identity not in self.reserved and identity not in self.completed
        with self.reservations.open('a') as handle:
            handle.write(json.dumps({'key': identity})+'\n')
            handle.flush()
            os.fsync(handle.fileno())
        self.reserved.add(identity)

    def remember(self, identifier, phase, prompt, answer):
        self.completed[key(identifier, phase, prompt)] = answer
