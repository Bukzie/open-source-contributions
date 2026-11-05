# Candidate 1: boxed/mutmut #596

| Field | Value |
|---|---|
| Upstream | https://github.com/boxed/mutmut/issues/596 |
| Title | Stats collection segfaults on Python 3.11 when a trampolined `__del__` runs during GC |
| Research date | 2026-11-04 |
| Stage | DISCOVER complete. VALIDATE not started. No implementation exists |
| Historical check (2026-11-04) | Open, 0 comments, no assignee, no PR, code positions confirmed on main. **Not current. Re-check before acting** |
| Research score | 6.85 (rank 1 of 6) |
| License | BSD-3-Clause |

## Problem
Since mutmut 3.7.0 the stats-mode trampoline sets and resets a `ContextVar` on every call, including `__del__`.
On CPython 3.10 and 3.11 the cyclic GC can re-enter `ContextVar.set()`, which produced exit 139, a `TypeError`
or "failed to collect stats".

## Proposed approach (a hypothesis, not agreed with maintainers)
Suspend the cyclic GC around `MutmutCallStack.set` and `reset` below Python 3.12, restoring prior state in a
`finally`. Alternative the maintainers may prefer: skip call-stack tracking inside `__del__`.

## Maintainer policy
No written AI policy. No ask-first rule. Issue threads are nearly silent; PRs are the working channel
(6 merges between 2026-10-15 and 2026-10-28, usually without formal review).

## Technical risks
- Per-call GC toggling overhead (must be measured)
- Thread safety of toggling global GC state
- Maintainers may prefer the smaller "skip `__del__`" change
- Needs a local Python 3.11 to reproduce
- A competing PR could appear (19 open PRs at the time)

## Next required decisions (owner)
1. Approve a fresh VALIDATE mission (see `docs/first-validation-mission-mutmut-596.md`)
2. Decide whether to post a short, owner-written comment on the issue before any PR

## Pointers
Executive report section 2.1 C1 and section 3 recommendation 1; ledger section 2.
