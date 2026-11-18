"""Allow testing the 15 remaining RMT pairs WITHOUT claiming independent review.

Place beside runner.py (after apply_rmt_tests.py and test_checkers.py).
Run: py enable_exploratory_15.py
No OpenAI API call is made by this script.

It labels the 15 revised pairs as exploratory_unreviewed, documents a source
correction for 4005 in BOTH prompts, and minimally extends runner.eligible().
All existing generated code / evaluation results / API logs remain untouched.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json
import shutil

ROOT = Path(__file__).resolve().parent
TASKS = ROOT / 'data' / 'tasks.json'
RUNNER = ROOT / 'runner.py'
IDS = {4002, 4005, 4008, 4011, 4014, 2, 5, 8, 11, 14, 3002, 3005, 3008, 3011, 3014}
OLD_RULE = "task.get('review_status') == 'approved_by_two_independent_reviewers'"
NEW_RULE = "task.get('review_status') in ('approved_by_two_independent_reviewers', 'exploratory_unreviewed')"
EXPLORATORY = 'exploratory_unreviewed'
NOTE = 'EXPLORATORY_ONLY: no independent review of prompt equivalence or clarity manipulation; not a validated confirmatory sample.'
SOURCE_NOTE = 'SOURCE_DEVIATION_4005: in both prompts corrected "not strictly inside the white sheet" to "strictly inside the white sheet"; see original contradictory source wording.'
NEEDLE = 'not strictly inside the white sheet'
FIX = 'strictly inside the white sheet'


def stop(message):
    raise SystemExit('STOP: ' + message)


def main():
    if not TASKS.is_file() or not RUNNER.is_file():
        stop('Place this file in the RMT_Batch_45 folder beside runner.py after importing tests.')
    try:
        tasks = json.loads(TASKS.read_text(encoding='utf-8'))
    except Exception as e:
        stop('Cannot parse data/tasks.json: ' + str(e))
    if not isinstance(tasks, list) or len(tasks) != 45 or len({t['problem_id'] for t in tasks}) != 45:
        stop('Expected 45 unique tasks; no changes made.')
    selected = [t for t in tasks if t.get('source_group') == 'revised_15']
    if {t['problem_id'] for t in selected} != IDS or len(selected) != 15:
        stop('Revised task IDs do not match expected 15; no changes made.')
    for t in selected:
        test = t.get('test_cases')
        if not (isinstance(test, dict) and isinstance(test.get('inputs'), list)
                and len(test['inputs']) > 0 and len(test['inputs']) == len(test.get('outputs', []))):
            stop(f"Task {t['problem_id']} is missing valid inputs/outputs. Run apply_rmt_tests.py first.")
        if not isinstance(t.get('clear_prompt'), str) or not isinstance(t.get('ambiguous_prompt'), str):
            stop(f"Task {t['problem_id']} has missing prompt text.")
    source = RUNNER.read_text(encoding='utf-8')
    if OLD_RULE not in source and NEW_RULE not in source:
        stop('Unknown runner.py version; refusing to patch automatically.')
    modified = False
    t4005 = next(t for t in selected if t['problem_id'] == 4005)
    counts = [t4005[cond].count(NEEDLE) for cond in ('clear_prompt', 'ambiguous_prompt')]
    if counts == [2, 2]:
        for c in ('clear', 'ambiguous'):
            if (ROOT/'generated'/f'4005_{c}.py').exists() or (ROOT/'logs'/f'4005_{c}.attempt.json').exists():
                stop('4005 has a prior generated solution/attempt; cannot change its original prompt.')
        for field in ('clear_prompt', 'ambiguous_prompt'):
            t4005[field] = t4005[field].replace(NEEDLE, FIX)
        if SOURCE_NOTE not in t4005.get('notes', []):
            t4005.setdefault('notes', []).append(SOURCE_NOTE)
        t4005['notes'] = [n for n in t4005['notes'] if n != 'source_description_contradiction: exclude until resolved identically']
        t4005['corrected_statement_at_utc'] = datetime.now(timezone.utc).isoformat()
        modified = True
    elif counts != [0, 0]:
        stop(f'Unexpected partial correction to 4005 prompts: {counts}. No changes made.')
    elif 'source_description_contradiction: exclude until resolved identically' in t4005.get('notes', []):
        stop('4005 contradiction flag exists but original phrase not found; review manually.')

    for t in selected:
        if t.get('review_status') == 'approved_by_two_independent_reviewers':
            stop(f"Task {t['problem_id']} already claims two independent reviews; refusing to relabel it.")
        if t.get('review_status') != EXPLORATORY:
            t['review_status'] = EXPLORATORY
            modified = True
        if NOTE not in t.get('notes', []):
            t.setdefault('notes', []).append(NOTE)
            modified = True
        # Deliberately preserve any 'independent_prompt_review_required' note and never invent reviewer names.

    next_source = source.replace(OLD_RULE, NEW_RULE) if OLD_RULE in source else source
    if next_source != source:
        next_source = next_source.replace('The 15 revised tasks without tests are excluded.',
                                          'Only eligible tasks are generated. Exploratory unreviewed pairs are labeled in the dataset.')
    if not modified and next_source == source:
        print('Already enabled. No changes needed. 15 pairs remain labeled exploratory_unreviewed.')
        return

    stamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    shutil.copy2(TASKS, TASKS.with_name(f'tasks.before_exploratory_{stamp}.json'))
    if next_source != source:
        shutil.copy2(RUNNER, RUNNER.with_name(f'runner.before_exploratory_{stamp}.py'))
    tmp = TASKS.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding='utf-8')
    tmp.replace(TASKS)
    if next_source != source:
        temp_runner = RUNNER.with_suffix('.py.tmp')
        temp_runner.write_text(next_source, encoding='utf-8')
        temp_runner.replace(RUNNER)
    report = ROOT / 'EXPLORATORY_15_DISCLOSURE.txt'
    report.write_text(
        'RMT: 15 revised task pairs tested in EXPLORATORY mode.\n'
        'No independent review has been conducted or claimed. The prompt\n'
        'equivalence and experimental clarity manipulation have not been\n'
        'independently validated. Do not describe these pairs as independently\n'
        'reviewed in the paper.\n'
        'Task 4005: corrected contradictory source phrase in BOTH prompts,\n'
        'with the original task wording otherwise preserved.\n'
        'Existing 60 generated code outputs and logs were not touched.\n',
        encoding='utf-8')
    print('OK: 15 revised pairs enabled for EXPLORATORY testing (NOT independently reviewed).')
    print('OK: all 45 tasks have input/output test cases.')
    print('OK: contradiction corrected identically in both 4005 prompts; documented.')
    print('OK: original tasks.json and runner.py backed up; existing generated code/logs/results untouched.')
    print('NEXT: py fast_generate_rmt.py --dry-run')
    print('THEN: py fast_generate_rmt.py --workers 3  (confirm PAID requests with RUN)')
    print('THEN: py runner.py evaluate --limit 90')
    print('THEN: py runner.py export')
    print('THEN: py runner.py status')


if __name__ == '__main__':
    main()
