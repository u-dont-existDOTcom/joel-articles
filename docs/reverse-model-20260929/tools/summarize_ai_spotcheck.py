"""Summarize completed primary GUI receipts without changing raw evidence."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


def main(root):
    selection_file = root / 'ai-spotcheck-selection.jsonl'
    selected = [json.loads(line) for line in selection_file.read_text().splitlines()]
    results_file = root / 'ai-spotcheck-pangram.jsonl'
    results = [json.loads(line) for line in results_file.read_text().splitlines()]
    assert len(selected) == len(results) == 20
    assert [r['id'] for r in selected] == [r['id'] for r in results]
    assert len({r['id'] for r in results}) == 20
    detail = []
    for source, result in zip(selected, results):
        assert hashlib.sha256(source['text'].encode()).hexdigest() == result['text_sha256'] == source['text_sha256']
        assert result['status'] == 'completed' and result['used_as_training_filter'] is False
        overview = result.get('primary_overview_text', '')
        metadata = '\n'.join(result.get('primary_ui_metadata', []))
        match = re.match(r'(Human Written|AI Assisted|AI Generated|Mixed|Human|AI)\b', overview)
        if not match:
            match = re.search(r'(Human Written|AI Assisted|AI Generated)\s+\d+\s+words scanned', metadata)
        label = match.group(1) if match else result['classification']
        assert label in {'Human Written', 'Human', 'AI Assisted', 'AI Generated', 'Mixed', 'AI'}
        detail.append({'id': result['id'], 'detailed_gui_label': label,
                       'captured_summary_label': result['classification'],
                       'human_pass': label in {'Human', 'Human Written'},
                       'credits': result['quoted_credits'], 'words_scanned': result['words_scanned']})
    counts = Counter(r['detailed_gui_label'] for r in detail)
    human = sum(r['human_pass'] for r in detail)
    credits = sum(r['credits'] for r in detail)
    assert 0 < credits <= 100
    summary = {'status': 'COMPLETE_STEP_2_MEASUREMENT_ONLY', 'selected': 20,
               'selection_sha256': hashlib.sha256(selection_file.read_bytes()).hexdigest(),
               'raw_results_sha256': hashlib.sha256(results_file.read_bytes()).hexdigest(),
               'detailed_label_counts': dict(counts), 'human_results': human,
               'ai_involvement_results': 20-human, 'ai_involvement_fraction': (20-human)/20,
               'pilot_credits_charged': credits, 'detector': 'Pangram 4.0 primary GUI',
               'training_filter': 'Only open-Qwen bidirectional fidelity judgments; no Pangram labels',
               'selection_limit': 'First 20 accepted training drafts by ID; early contiguous source sample, not a representative random sample',
               'interpretation': 'Untrained generated-data diagnostic, not either adapter pass rate. AI-assisted involvement is distinct from fully AI-generated.',
               'label_handling': 'Prefer detailed primary Overview header; retain captured broader history label in raw receipts.',
               'cases': detail}
    root.joinpath('ai-spotcheck-summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({key: summary[key] for key in ['status', 'detailed_label_counts', 'human_results', 'ai_involvement_results', 'pilot_credits_charged']}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--evaluation', type=Path, required=True)
    main(parser.parse_args().evaluation)
