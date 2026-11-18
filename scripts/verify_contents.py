#!/usr/bin/env python3
"""Read-only checks of file integrity and study artifact counts. No code execution or network calls."""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def sha(path: Path): return hashlib.sha256(path.read_bytes()).hexdigest()

def check_hash_manifest():
    original_root = ROOT / 'extended_135'
    manifest = json.loads((original_root / 'MANIFEST_SHA256.json').read_text(encoding='utf-8'))['files']
    problems=[]
    for rel, attrs in manifest.items():
        f=original_root / rel
        if not f.is_file() or f.stat().st_size!=attrs['size'] or sha(f)!=attrs['sha256']:
            problems.append(rel)
    if problems: raise SystemExit(f'FAILED: extended original manifest: {problems[:5]}')
    print(f'OK: original extended evidence manifest: {len(manifest)} files')

def check_release_hashes():
    lines=(ROOT/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines()
    problems=[]
    for line in lines:
        h,rel=line.split('  ',1)
        f=ROOT/rel
        if not f.is_file() or sha(f)!=h:problems.append(rel)
    if problems:raise SystemExit(f'FAILED: packaged checksums: {problems[:5]}')
    print(f'OK: packaged SHA-256 manifest: {len(lines)} files')

def check_counts():
    tasks=json.loads((ROOT/'initial_45/data/tasks.json').read_text(encoding='utf-8'))
    initial_ids={str(t['problem_id']) for t in tasks}
    paths=list((ROOT/'initial_45/generated').glob('*.py'))
    judgments=list((ROOT/'initial_45/results').glob('*.json'))
    initial_tests=sum(len(t['test_cases']['inputs']) for t in tasks)
    assert len(initial_ids)==45 and len(paths)==90 and len(judgments)==90 and initial_tests==5866
    initial_results=[json.loads(p.read_text(encoding='utf-8')) for p in judgments]
    initial_pass=sum(int(x['pass_at_1']) for x in initial_results)
    initial_executions=sum(int(x['passed_before_first_failure'])+(not bool(x['pass_at_1'])) for x in initial_results)
    extended=ROOT/'extended_135/benchmark'
    code=list((extended/'outputs').glob('person_*/generated/*.py'))
    verdicts=list((extended/'outputs').glob('person_*/results/*.json'))
    tests=list((extended/'data/test_cases').glob('person_*/*.json'))
    extended_ids=set()
    for t in tests:extended_ids.add(str(json.loads(t.read_text(encoding='utf-8'))['problem_id']))
    assert not(initial_ids & extended_ids),f'Overlapping task IDs: {sorted(initial_ids & extended_ids)}'
    assert len(code)==270 and len(verdicts)==270 and len(tests)==135 and len(extended_ids)==135
    extended_inputs=sum(len(json.loads(t.read_text(encoding='utf-8'))['inputs']) for t in tests)
    extended_results=[json.loads(t.read_text(encoding='utf-8')) for t in verdicts]
    extended_pass=sum(int(x['pass_at_1']) for x in extended_results)
    extended_executions=sum(int(x['test_cases_executed']) for x in extended_results)
    assert (initial_pass, extended_pass, extended_inputs, initial_executions, extended_executions)==(87,260,8665,11724,17208)
    print(f'OK: initial 45 tasks / 90 solutions / 5,866 unique cases / {initial_pass} raw passes')
    print(f'OK: extended 135 tasks / 270 solutions / 8,665 unique cases / {extended_pass} raw passes')
    print(f'OK: combined {len(initial_ids|extended_ids)} tasks / {len(paths)+len(code)} solutions / {initial_tests+extended_inputs} unique cases')
    print(f'INFO: historical raw passes = {initial_pass+extended_pass}/360; reconstructed executed checks = {initial_executions+extended_executions}')
    print('INFO: numbers are raw archived verdicts; see docs/KNOWN_LIMITATIONS.md')

if __name__=='__main__':
    check_hash_manifest()
    check_release_hashes()
    check_counts()
