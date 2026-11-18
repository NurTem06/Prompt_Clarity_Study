"""Non-network unit checks. Run: py test_checkers.py"""
import json
from pathlib import Path
from inside_judge import validate_output

base=Path(__file__).parent
all_tasks=json.loads((base/'data/tasks.json').read_text(encoding='utf-8'))
count=0
for task in all_tasks:
    if task['test_cases'] is None:continue
    for inp,answer in zip(task['test_cases']['inputs'],task['test_cases']['outputs']):
        valid,detail=validate_output(task['problem_id'],inp,answer,answer)
        assert valid,(task['problem_id'],detail)
        count+=1
print(f'OK: all {count} provided reference-output test cases pass their checker self-test.')
