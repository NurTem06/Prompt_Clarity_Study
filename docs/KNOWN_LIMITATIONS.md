# Known limitations and reconciliation notes

**Important:** This package preserves source data and reports exactly as supplied. Packaging does not resolve experimental uncertainty, adjudicate edge cases, or change Pass@1 figures.

## Archived counts (not revised statistical conclusions)

- Initial 45: **90** code files / **90** verdict records; **87** verdicts with `pass_at_1=1`; **5,866** unique input/output cases. The 45-task judge uses early stopping. Reconstructing attempted cases from `passed_before_first_failure` plus the first failed case yields **11,724** executions.
- Extended 135: **270** code files / **270** verdict records; **260** verdicts with `pass_at_1=1`; **8,665** unique input/output cases and **17,208** recorded executions.
- Combined: 180 tasks, 360 code files, 14,531 unique test cases, **28,932** executed checks reconstructed from these archival verdicts; 347/360 raw binary success outcomes.

The current paper and slide draft circulated by the team state **28,940** executed checks and **349/360** successes (175 Clear, 174 Ambiguous). Those numbers **do not equal** the immutable archived raw verdict totals and should not be claimed as direct raw-log sums. This package does not create an undocumented replacement set of verdicts. Reconcile paper figures using a documented checker version and case-by-case changes before final submission.

## Specific validity concerns identified in earlier independent review

- **Task 3058:** candidate outputs accepted by semantic verification despite reference-token disagreement. A false-rejection risk exists if only the reference string is compared.
- **Task 3048:** supplied case 4 violates the problem's tree constraint (contains a cycle, duplicate edge and isolated nodes). The mismatch should not automatically be attributed to the generated programs.
- **Task 3041:** a boundary condition at exactly 10,000 seconds remained disputed; seek an authoritative interpretation.
- **Task 4021:** the source is an intentionally mysterious puzzle with no conventional objective; study suitability warrants review.
- **Task 3034:** an actual large numeric mismatch was recorded against a reference example.
- Five additional reference-only classifications were overly conservative and merit documented uniqueness review (IDs 23, 3021, 4046, 59, 3047).

These findings describe an **audit of saved results**, not new API generations and not a fully rejudged, finalized unified dataset. Data provenance in the archive is recorded but is not absolute proof that every input is from an unmodified upstream APPS task. The initial batch also includes exploratory prompts that were not independently reviewed for semantic equivalence.

## Reproducibility caveats

- The extended archive stores generated code, paired prompts, test files, checkers, verdicts, original pipeline scripts, and SHA-256 provenance. It does not independently authenticate every original API exchange.
- Pass@1 is correctness on **available tests**, not a proof for all possible inputs or hidden judge cases.
- A non-significant McNemar result is not evidence that two prompting conditions are equivalent.
- Code is potentially untrusted. Keep evaluation in an isolated, network-disabled Docker container.
- Scripts under `extended_135/original_workflow/` preserve paths from their original `RMT_Final_v2` workspace and are included for source-level reproducibility; they are not guaranteed to run unchanged after this cleanup. Some original scripts predate the final evaluation and have historical comments about missing tests. Read source versions and do not re-run paid generation to recreate frozen first attempts.
