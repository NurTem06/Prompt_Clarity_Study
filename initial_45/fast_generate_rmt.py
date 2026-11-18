"""Parallel first-attempt generation for the existing RMT_Batch_45 project.

Place this file next to runner.py and run:
  py fast_generate_rmt.py --workers 3

It calls the existing runner.py in separate processes for different tasks,
retaining its original model, prompting, attempt logs and retry safeguards.
"""
import argparse
import os
from pathlib import Path
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from runner import load, eligible, GEN, LOG, BASE


def pending_conditions(task):
    out = []
    for condition in ('clear', 'ambiguous'):
        stem = f"{task['problem_id']}_{condition}"
        if not (GEN / f'{stem}.py').exists() and not (LOG / f'{stem}.attempt.json').exists():
            out.append(condition)
    return out


def process_one(task):
    task_id = task['problem_id']
    # Limit 2 per task; original runner skips prior code or attempted requests.
    cmd = [sys.executable, str(BASE/'runner.py'), 'generate', '--task', str(task_id), '--limit', '2', '--yes']
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=BASE)
    missing = []
    for condition in ('clear', 'ambiguous'):
        if not (GEN/f'{task_id}_{condition}.py').exists():
            missing.append(condition)
    return task_id, result.returncode, missing, result.stdout, result.stderr


def main():
    parser = argparse.ArgumentParser(description='Generate eligible prompts concurrently while preserving first attempts.')
    parser.add_argument('--workers', type=int, default=3, help='Concurrent tasks (default: 3, recommend <=3).')
    parser.add_argument('--dry-run', action='store_true', help='List pending prompts without API requests.')
    args = parser.parse_args()

    if not 1 <= args.workers <= 4:
        parser.error('--workers must be between 1 and 4')
    selected = [(t, pending_conditions(t)) for t in load() if eligible(t)]
    selected = [(t, conditions) for t, conditions in selected if conditions]
    n_requests = sum(len(conditions) for _, conditions in selected)
    print(f'Pending: {n_requests} paid API requests across {len(selected)} tasks.', flush=True)
    print('Excluded: tasks missing official tests or independent review.', flush=True)
    if selected:
        print('Task IDs: ' + ', '.join(str(t['problem_id']) for t,_ in selected), flush=True)

    if args.dry_run or not selected:
        return 0
    if not os.environ.get('OPENAI_API_KEY'):
        print('ERROR: OPENAI_API_KEY is not set in this PowerShell session.', file=sys.stderr)
        return 2
    confirm = input(f'Type RUN to submit up to {n_requests} PAID requests ({args.workers} concurrent tasks): ').strip()
    if confirm != 'RUN':
        print('Cancelled; no requests sent.')
        return 0
    failures=[]
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(process_one, t): t['problem_id'] for t,_ in selected}
        for future in as_completed(futures):
            task_id, status, missing, stdout, stderr = future.result()
            if status == 0 and not missing:
                print(f'[OK] Task {task_id}: both solutions saved', flush=True)
            else:
                failures.append(task_id)
                print(f'[CHECK] Task {task_id}: missing outputs {missing}, exit={status}', flush=True)
                if stderr:
                    print(stderr[-650:], flush=True)
                if stdout:
                    print(stdout[-300:], flush=True)
    print(f'Batch complete. Tasks requiring review: {failures or "none"}', flush=True)
    print('NEXT: py runner.py evaluate --limit 90', flush=True)
    print('THEN: py runner.py export', flush=True)
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
