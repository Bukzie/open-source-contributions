# Verification standards

- **Bind every claim** to a source, a method and a date. Example: "open, unassigned, checked 2026-11-04 via
  read-only `gh issue view`".
- **Historical is not current.** A status older than a day or two is a lead, not a fact. Re-check before acting.
- **Labels.** VERIFIED (re-observed with cited evidence), REFUTED, PARTIAL, UNVERIFIED (not re-checked; treat as
  opinion). The research ledger uses these.
- **Reproduction first** for any defect fix. Keep the minimal repro and its output.
- **Tests** run locally on the final implementation SHA. Report what ran and what did not.
- **Independent review** is bound to the exact SHA reviewed. A material contributor cannot review the same
  candidate.
- **QE Gate** results are advisory evidence only, and only when the candidate binding and provenance are
  understood. They do not approve or replace upstream CI.
- **Reconstructions** (for example the wildcard report) are labelled as such and never presented as original work.
