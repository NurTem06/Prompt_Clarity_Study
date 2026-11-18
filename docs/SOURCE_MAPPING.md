# File origins and cleaning decisions

| Supplied archive | Retained under | Handling |
|---|---|---|
| `RMT_Batch_45(3).zip` | `initial_45/` | Preserved final `tasks.json`, first-attempt code, generation logs, per-run verdicts, results CSV, primary runner/judge/checker scripts, and disclosures. Removed dated backups, bytecode, redundant scripts, and outdated readmes. |
| `RMT_Final_v2.zip` | `extended_135/` | Selected nested `RMT_APPS_FULL_EVIDENCE.zip` as the canonical 135-task evidence snapshot; retained all original 708 archive files including the 707-file SHA-256 manifest, plus source Markdown prompt provenance, preflight records and the original import/orchestration scripts. Omitted nested archive duplicates, `outputs/` and `RMT_APPS_Benchmark/` duplicate copies, local `.pyc`, and old launch wrappers. |
| `RMT_Pilot_4004(2).zip` | `pilot_provenance/` | Retained only unique three-pilot input and API metadata/response JSONs. The six identical pilot `.py` files already exist in `initial_45/generated/`. Excluded duplicated runner/judge and requirements files. |

No generated `.py` file or saved verdict JSON was modified to change a result. Original filenames and provenance inside each cohort are maintained. The project README and integrity checker are new packaging utilities, **not** original experiment code.
