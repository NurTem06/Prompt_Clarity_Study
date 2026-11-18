# RMT Final — APPS Original Test Case Evaluation

Generated UTC: 2026-11-18T01:03:34.026794+00:00

**Test source:** APPS test split, retrieved by problem_id from Hugging Face metr-evals/apps with verified problem metadata.

## Results per person

| Person | Tested programs | Benchmark checker passed | Validated denominator | Validated passed |
|---|---:|---:|---:|---:|
| person_1 | 90/90 | 88/90 | 86 | 84 |
| person_2 | 90/90 | 86/90 | 90 | 86 |
| person_3 | 90/90 | 86/90 | 82 | 80 |

## Matched pairs by difficulty

| Participant / tier | Validated pairs | Both pass | Clear only | Ambiguous only | Both fail |
|---|---:|---:|---:|---:|---:|
| person_1/introductory | 15 | 14 | 0 | 0 | 1 |
| person_1/interview | 14 | 14 | 0 | 0 | 0 |
| person_1/competition | 14 | 14 | 0 | 0 | 0 |
| person_2/introductory | 15 | 15 | 0 | 0 | 0 |
| person_2/interview | 15 | 15 | 0 | 0 | 0 |
| person_2/competition | 15 | 13 | 0 | 0 | 2 |
| person_3/introductory | 14 | 14 | 0 | 0 | 0 |
| person_3/interview | 14 | 14 | 0 | 0 | 0 |
| person_3/competition | 13 | 12 | 0 | 0 | 1 |

## Methodological qualifications

1. All generated solutions were frozen before retrieving test cases. No new OpenAI requests are made.
2. All available **APPS dataset inputs/outputs** are used; they are not merely the examples in problem statements.
3. For construction tasks, reviewed validators check the task rules. Tasks requiring further checker review are excluded from validated Pass@1.
4. APPS cases may be limited and are not necessarily the complete private online judge. Pass@1 here means success on the evaluated APPS test suite.
5. Tests with missing source data, unmatched metadata or checker errors are reported as not evaluated; neither success nor failure is invented.

**Raw task-level results:** `APPS_270_Results.csv` and the three participant CSV files.
**Full test suites:** `data/test_cases/person_*/<problem_id>.json` inside `RMT_APPS_Benchmark`.

## Cases still requiring manual review

- person_1 / 23: exact-reference comparison only; multi-output correctness cannot be certified.
- person_1 / 3021: exact-reference comparison only; multi-output correctness cannot be certified.
- person_3 / 4046: exact-reference comparison only; multi-output correctness cannot be certified.
- person_3 / 59: exact-reference comparison only; multi-output correctness cannot be certified.
- person_3 / 3047: exact-reference comparison only; multi-output correctness cannot be certified.
- person_3 / 3058: exact-reference comparison only; multi-output correctness cannot be certified.
