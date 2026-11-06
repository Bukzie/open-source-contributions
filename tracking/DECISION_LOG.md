# Decision log

Append-only. One entry per decision that changes scope, sequence, or publication. Newest last.

## 2026-11-04: Research run completed
Six candidates shortlisted, two weak survivors held in backlog, remainder rejected. No GitHub writes were made.
See `../research/summaries/EXECUTIVE_REPORT.md`.

## 2026-11-05: Repository prepared locally
- Raw evidence archive (about 200 files, 7 MB, contains third-party comment text and unreviewed agent output)
  kept outside the tracked tree. Curated reports, executive report and ledger published with local paths scrubbed.
- Missing wildcard report documented as missing; a clearly labelled reconstruction was added instead.
- Initial tracked state is local only. Creating the GitHub repository, pushing, and creating Project items are
  **pending owner approval**.

## 2026-11-05: mutmut #596 validation completed
Owner authorized a read-only validation. Result: crash reproduced deterministically on 3.11, absent on 3.12 and on
mutmut 3.6.0. Recommendation GO to the next owner decision. No implementation, fork, comment or PR was made.
Evidence: `candidates/evidence/mutmut-596/2026-11-05/`.
