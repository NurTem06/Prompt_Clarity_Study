# Prompt Clarity and Functional Correctness of LLM-Generated Python Code

Research Methods and Tools — Group SE-2413, Astana IT University.

This repository is a **cleaned evidence release** combining the three original archives:
`RMT_Pilot_4004(2).zip`, `RMT_Batch_45(3).zip`, and `RMT_Final_v2.zip`.
Nested ZIPs, duplicate program copies, superseded backups, bytecode caches, and obsolete launch wrappers were omitted. **Saved code and archived judge verdicts have not been modified or replaced.**

## At a glance

| Cohort | Distinct APPS tasks | Saved first-attempt Python solutions | Unique test inputs | Archived raw pass count |
|---|---:|---:|---:|---:|
| Initial cohort | 45 | 90 | 5,866 | 87 / 90 |
| Extended cohort | 135 | 270 | 8,665 | 260 / 270 |
| **Combined** | **180** | **360** | **14,531** | **347 / 360 (raw archived verdicts)** |

Two conditions are compared for each task: **Clear** and **Ambiguous**. These counts document files and verdicts preserved in the supplied archives; the archive alone cannot independently verify every underlying model API request. The published/slide figures may use later semantic rejudging and **must not be silently conflated with the raw totals above**. See [KNOWN_LIMITATIONS.md](docs/KNOWN_LIMITATIONS.md).

## Repository structure

```text
initial_45/
  data/tasks.json           # 45 paired task specifications and test suites
  generated/               # 90 saved Python code files
  results/                 # 90 per-solution verdict JSONs
  logs/                    # available raw generation response/attempt records
  results.csv               # original raw cohort table
  runner.py                 # original pipeline (generation is paid)
  inside_judge.py           # original isolated judge
  test_checkers.py          # offline checker self-test
  test_audit_45.csv         # validation notes
extended_135/
  benchmark/
    data/                   # 135 prompt pairs, official-source test suites, checkers
    outputs/person_*/       # 270 frozen generated scripts + verdicts
    APPS_270_Results.csv    # original raw extended-cohort table
    APPS_Report.md          # audit and outcome report
    runner_final.py         # original generation runner
    inside_judge_final.py   # original Docker judge
  MANIFEST_SHA256.json      # original 707-file evidence manifest
  source_markdown/          # original prompt sources
  original_workflow/        # original import, evaluation and orchestration scripts
  preflight_audit/          # source/prompt review records
pilot_provenance/           # distinct API-response evidence for 3 early pilots
scripts/verify_contents.py # read-only archive integrity and cohort counts
SHA256SUMS.txt              # hashes of packaged files
```

The three pilot tasks (IDs 4004, 4, 3004) are **already included in the initial 45**. Only their unique request/response metadata is in `pilot_provenance/`; their generated `.py` scripts are not repeated.

## Inspect or reproduce

1. Clone/unzip this repository and verify file integrity (no API calls, no execution of generated code):
   ```bash
   python scripts/verify_contents.py
   ```
2. Read `initial_45/results.csv`, `extended_135/benchmark/APPS_270_Results.csv`, and the matching verdict JSON files.
3. Inspect paired prompts in `initial_45/data/tasks.json` and `extended_135/benchmark/data/person_*_prompts.json`.
4. To investigate checking behavior, inspect the original Docker-based judges. **Do not run model-generated programs directly on your host.** Re-execution requires Docker, the Python environment used for the judge, and confirmation of checker and dataset versions.
5. To generate *new* model responses rather than inspect existing ones, the original runners require credentials and can incur API charges. That is not necessary to audit the saved code or reports.

The extended evidence's original SHA-256 manifest is verified relative to the `extended_135/` directory. Run the verification script after making any changes to identify modified evidence.

## Data origins and integrity

- Tasks and test cases are identified as APPS benchmark data (`metr-evals/apps` test split); the archive includes IDs and source links. Not every remote record was independently reauthenticated.
- The initial 45-task stage includes exploratory/unreviewed prompt pairs, explicitly labeled in the source metadata.
- This is an **academic evidence archive**, not a production service or an independent certificate of model correctness.
- No dataset license is asserted here. Check the upstream APPS dataset and any third-party problem statements before redistributing them outside the course.

## Study methods and known issues

Read [Methods addendum](docs/REPRODUCIBILITY_METHODOLOGY_EN.md) and [Known limitations](docs/KNOWN_LIMITATIONS.md) before citing pass rates. Do not present the test-suite results as proof of correctness on unseen cases. The original archived verdicts are frozen; any corrected semantic evaluation should be published as a *new, clearly labeled* results version.
