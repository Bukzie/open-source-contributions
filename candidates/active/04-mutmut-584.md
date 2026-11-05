# Candidate 4: boxed/mutmut #584

| Field | Value |
|---|---|
| Upstream | https://github.com/boxed/mutmut/issues/584 |
| Title | Process pools started by tests outlive every mutant |
| Research date | 2026-11-04 |
| Stage | DISCOVER complete. VALIDATE not started. No implementation exists |
| Historical check (2026-11-04) | Open, 0 comments, no PR; reporter offered a PR six weeks earlier and had not opened one. **Not current. Re-check before acting** |
| Research score | 6.65 (rank 4 of 6) |
| License | BSD-3-Clause |

## Problem
Forked mutant runs end with `os._exit()` and share mutmut's process group, so joblib, `multiprocessing.Pool`
and `ProcessPoolExecutor` children survive each mutant (reporter saw 8,359 orphans on one run).

## Proposed approach (a hypothesis)
`os.setpgid(0, 0)` in the child after fork; after reaping, `os.killpg` with SIGTERM then optional SIGKILL; signal
the group on timeout. POSIX only.

## Maintainer policy
Same as candidate 1: no written AI policy, PR is the working channel.

## Technical risks
Race between `setpgid` and `killpg`; interplay with the September process-isolation feature; terminal process
group nuance; the reporter may still submit their own PR.

## Next required decisions (owner)
1. Whether to ask the reporter (owner-written) if they still intend to submit
2. Sequence relative to candidate 1

## Pointers
Executive report section 2.1 C4; ledger section 2.
