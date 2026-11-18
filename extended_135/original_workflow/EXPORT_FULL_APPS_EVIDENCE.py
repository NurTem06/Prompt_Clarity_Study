"""Package frozen RMT programs, APPS test suites, code and verdicts for reproducibility.

Only local files are read. No network, Docker or OpenAI calls are made.
"""
from __future__ import annotations
from pathlib import Path
import hashlib
import json
import zipfile
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parent
BENCH=ROOT/'RMT_APPS_Benchmark'
OUTPUT=ROOT/'RMT_APPS_FULL_EVIDENCE.zip'


def main():
    if not (BENCH/'APPS_270_Results.csv').is_file():
        print('No benchmark result CSV yet; skip full evidence export.')
        return 2
    files=[]
    for name in ('APPS_270_Results.csv','APPS_summary.json','APPS_Report.md','APPS_import_log.json',
                 'runner_final.py','inside_judge_final.py','config.json'):
        p=BENCH/name
        if p.is_file():files.append(p)
    for person in ('person_1','person_2','person_3'):
        p=BENCH/f'{person}_APPS_results.csv'
        if p.is_file(): files.append(p)
        task_source=BENCH/'data'/f'{person}_prompts.json'
        if task_source.exists():files.append(task_source)
        for suffix in (f'data/test_cases/{person}',f'outputs/{person}/generated',
                       f'outputs/{person}/results'):
            base=BENCH/suffix
            if base.is_dir():files.extend(base.glob('*.json') if suffix.endswith('results') or 'test_cases' in suffix else base.glob('*.py'))
    checkers=BENCH/'data'/'checkers'
    if checkers.is_dir():files.extend(checkers.glob('*.py'))
    ownchecker=ROOT/'validated_apps_checkers.py'
    if ownchecker.exists():files.append(ownchecker)
    files=sorted(set(files),key=lambda x:x.as_posix())
    metadata={'created_utc':datetime.now(timezone.utc).isoformat(),'files':{}}
    temp=OUTPUT.with_name(OUTPUT.name+'.tmp')
    with zipfile.ZipFile(temp,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
        for p in files:
            arcname=('benchmark/' + p.relative_to(BENCH).as_posix()) if p.is_relative_to(BENCH) else p.name
            z.write(p,arcname)
            metadata['files'][arcname]={'size':p.stat().st_size, 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
        z.writestr('MANIFEST_SHA256.json',json.dumps(metadata,indent=2,ensure_ascii=False)+'\n')
    temp.replace(OUTPUT)
    print('Full reproducibility archive:',OUTPUT)
    print('Archived',len(files),'files; size', round(OUTPUT.stat().st_size/1048576,2),'MiB')
    return 0


if __name__=='__main__':raise SystemExit(main())
