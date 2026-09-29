"""Deterministic licensed-source sampling, before any model calls."""
import argparse
import collections
import hashlib
import json
import random
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

SEED = 3407
LICENSES = {
    "OANC": {"license": "Unrestricted use and redistribution, including commercial use",
             "source": "https://anc.org/data/oanc/",
             "archive_url": "https://github.com/nancyide/anc-website/releases/download/datasets-2026-09-25/OANC_GrAF.zip"},
    "MASC": {"license": "CC BY 3.0 US",
             "license_url": "https://creativecommons.org/licenses/by/3.0/us/",
             "source": "https://anc.org/data/masc/",
             "attribution": "Manually Annotated Sub-Corpus, American National Corpus; Nancy Ide and Keith Suderman. Source paths and available original-author metadata retained.",
             "archive_url": "https://github.com/nancyide/anc-website/releases/download/datasets-2026-09-25/masc_500k_texts.zip"},
}

def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()

def normalized(text):
    return " ".join(re.findall(r"\w+", text.casefold()))

def passages(text):
    # Preserve literal source spans. Long blocks are split at punctuation,
    # short consecutive blocks may form one passage. No paraphrasing occurs.
    # Delimiter scanning is linear even when a document ends in one newline.
    # The former whole-block lookahead could repeatedly rescan that last block.
    blocks = []
    cursor = 0
    boundaries = [(m.start(), m.end()) for m in re.finditer(r"\n[ \t\r]*\n+", text)]
    for end, following in boundaries + [(len(text), len(text))]:
        block = text[cursor:end]
        a = cursor + len(block) - len(block.lstrip())
        b = end - (len(block) - len(block.rstrip()))
        if a < b:
            blocks.append((a, b))
        cursor = following
    candidates = []
    start = None
    end = None
    for a, b in blocks:
        parts = [(a, b)]
        if len(text[a:b].split()) > 250:
            bounds = [a] + [a + m.end() for m in re.finditer(r"[.!?][\"')]*\s+", text[a:b])] + [b]
            parts = [(x, y) for x, y in zip(bounds, bounds[1:]) if x < y]
        for x, y in parts:
            if start is not None and len(text[start:y].split()) > 250:
                if 100 <= len(text[start:end].split()) <= 250:
                    candidates.append((start, end))
                start = None
            if len(text[x:y].split()) > 250:
                continue
            if start is None:
                start = x
            end = y
            if 140 <= len(text[start:end].split()) <= 250:
                candidates.append((start, end))
                start = None
    if start is not None and 100 <= len(text[start:end].split()) <= 250:
        candidates.append((start, end))
    return [(a, b) for a, b in candidates if len(re.findall(r"[A-Za-z]+", text[a:b])) >= 80]

def genre(path, corpus):
    category = path.split("/")[3 if corpus == "OANC" else 2]
    if category in {"fiction", "ficlets", "spam", "jokes", "movie-script", "twitter"}:
        return None
    if category == "email":
        return "email"
    if category == "letters":
        return "letters"
    if category in {"technical", "govt-docs"}:
        return "technical"
    if category in {"travel_guides", "travel-guides"}:
        return "practical"
    if category == "newspaper:newswire":
        return "news"
    return "essays_journal"

def build(corpus_dir, output_dir):
    rng = random.Random(SEED)
    documents = []
    archives = []
    excluded_sources = []
    for corpus, filename in [("OANC", "OANC_GrAF.zip"), ("MASC", "masc_500k_texts.zip")]:
        path = corpus_dir / filename
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            for name in sorted(names):
                if not name.endswith(".txt") or (corpus == "OANC" and "/written_" not in name) or (corpus == "MASC" and "/written/" not in name):
                    continue
                category = genre(name, corpus)
                if category is None:
                    continue
                raw = archive.read(name)
                text = raw.decode("utf-8-sig", errors="strict")
                options = passages(text)
                if not options:
                    continue
                metadata = {}
                header_name = name[:-4] + ".anc"
                if header_name in names:
                    try:
                        root = ET.fromstring(archive.read(header_name))
                    except ET.ParseError as error:
                        excluded_sources.append({"corpus": corpus, "path": name,
                                                 "reason": "Malformed source metadata",
                                                 "detail": str(error)})
                        continue
                    for element in root.iter():
                        key = element.tag.split("}")[-1]
                        if key in {"title", "author", "publisher", "pubDate", "eAddress"} and element.text:
                            metadata.setdefault(key, []).append(element.text.strip())
                documents.append({"corpus": corpus, "path": name,
                                  "document_sha256": sha(raw), "text": text,
                                  "normalized": normalized(text), "options": options,
                                  "genre": category, "metadata": metadata})
        archives.append({"filename": filename, "sha256": sha(path.read_bytes()), "bytes": path.stat().st_size,
                         "corpus": corpus, **LICENSES[corpus]})
        print(json.dumps({"read_corpus": corpus, "eligible_documents_so_far": len(documents),
                          "excluded_metadata": len(excluded_sources)}), flush=True)
    parent = list(range(len(documents)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def union(a, b):
        parent[find(b)] = find(a)
    identities = {}
    duplicate_links = []
    for i, doc in enumerate(documents):
        for key in [("stem", Path(doc["path"]).stem.casefold()), ("content", sha(doc["normalized"]))]:
            if key in identities:
                union(i, identities[key])
                duplicate_links.append({"a": doc["path"], "b": documents[identities[key]]["path"], "reason": key[0]})
            else:
                identities[key] = i
    # MASC often contains excerpts rather than whole OANC documents. Search
    # literal normalized snippets at different positions, independent of offset.
    oanc = [i for i, d in enumerate(documents) if d["corpus"] == "OANC"]
    for i, doc in enumerate(documents):
        if doc["corpus"] != "MASC":
            continue
        words = doc["normalized"].split()
        probes = [" ".join(words[p:p+30]) for p in [10, len(words)//2, max(0, len(words)-40)] if p+30 <= len(words)]
        for j in oanc:
            if find(i) == find(j):
                continue
            if sum(probe in documents[j]["normalized"] for probe in probes) >= 2:
                union(i, j)
                duplicate_links.append({"a": doc["path"], "b": documents[j]["path"], "reason": "MASC excerpt containment"})
    groups = collections.defaultdict(list)
    for i in range(len(documents)):
        groups[find(i)].append(i)
    eligible = collections.defaultdict(list)
    for members in groups.values():
        # Retain MASC as the representative when both corpora provide it.
        members.sort(key=lambda i: (documents[i]["corpus"] != "MASC", documents[i]["path"]))
        doc = documents[members[0]]
        doc["aliases"] = [{"corpus": documents[i]["corpus"], "path": documents[i]["path"],
                           "sha256": documents[i]["document_sha256"], "metadata": documents[i]["metadata"]} for i in members]
        doc["document_id"] = sha("\n".join(sorted(a["path"] for a in doc["aliases"])))
        eligible[doc["genre"]].append(doc)
    quotas = {"email": 50, "letters": 150, "news": 50, "technical": 280,
              "practical": 170, "essays_journal": 500}
    selected = []
    remainder = []
    for category, docs in sorted(eligible.items()):
        rng.shuffle(docs)
        take = min(quotas.get(category, 0), len(docs))
        selected.extend(docs[:take])
        remainder.extend(docs[take:])
    rng.shuffle(remainder)
    selected.extend(remainder[:1200-len(selected)])
    assert len(selected) == 1200, f"Only {len(selected)} eligible source documents"
    rng.shuffle(selected)
    records = []
    for index, doc in enumerate(selected):
        a, b = rng.choice(doc["options"])
        text = doc["text"][a:b].strip()
        # Freeze source groups and split before constructing counterpart pairs.
        split = "train" if index < 1000 else "dev" if index < 1100 else "test"
        records.append({"id": f"H{index+1:04d}", "split": split,
                        "document_id": doc["document_id"], "corpus": doc["corpus"],
                        "source_path": doc["path"], "source_sha256": doc["document_sha256"],
                        "source_aliases": doc["aliases"], "genre": doc["genre"],
                        "start_char": a, "end_char": b, "human": text,
                        "human_sha256": sha(text), "words": len(text.split()),
                        "license": LICENSES[doc["corpus"]]["license"],
                        "metadata": doc["metadata"],
                        "method": "paraphrase" if index % 3 == 0 else "notes_regeneration"})
    assert len({r["document_id"] for r in records}) == 1200
    assert len({r["human_sha256"] for r in records}) == 1200
    for split, count in [("train", 1000), ("dev", 100), ("test", 100)]:
        assert sum(r["split"] == split for r in records) == count
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "human-passages.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records))
    manifest = {"seed": SEED, "archives": archives, "passages": len(records),
                "splits": dict(collections.Counter(r["split"] for r in records)),
                "genres": dict(collections.Counter(r["genre"] for r in records)),
                "corpora": dict(collections.Counter(r["corpus"] for r in records)),
                "methods": dict(collections.Counter(r["method"] for r in records)),
                "eligible_document_groups": len(groups), "deduplication_links": duplicate_links,
                "excluded_sources": excluded_sources,
                "manifest_sha256": sha((output_dir / "human-passages.jsonl").read_bytes()),
                "PG19_fraction": 0, "generated_pairs": 0}
    (output_dir / "corpus-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({k:v for k,v in manifest.items() if k not in {"archives", "deduplication_links"}}, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpora", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build(args.corpora, args.output)
