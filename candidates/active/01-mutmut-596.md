# Candidate 1: boxed/mutmut #596

| Field | Value |
|---|---|
| Upstream | https://github.com/boxed/mutmut/issues/596 |
| Title | Stats collection segfaults on Python 3.11 when a trampolined `__del__` runs during GC |
| Research date | 2026-11-04 |
| Stage | IMPLEMENT (local candidate only, owner-approved 2026-11-06). Nothing posted, forked or submitted upstream |
| Historical check (2026-11-04) | Open, 0 comments, no assignee, no PR, code positions confirmed on main. Superseded by the 2026-11-05 validation below |
| Validation (2026-11-05) | See section below and `evidence/mutmut-596/2026-11-05/`. Upstream SHA `857019a`. **Re-check issue and PRs again before any action** |
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

## Validation result (2026-11-05, read-only)
- Upstream state unchanged: open, no assignee, no comments, no competing PR, no AI policy found, no ask-first rule.
- Reproduced on macOS arm64, Python 3.11.16, mutmut 3.8.1: segfault in 10 of 10 trials (deterministic, not intermittent here). Python 3.12.13: 5 of 5 pass. mutmut 3.6.0 on 3.11: 3 of 3 pass.
- Baseline suite: 473 passed and 2 failed on 3.12; 472 passed, 3 failed and 1 error on 3.11. None of the failures was tied to this issue; the cause of the extra 3.11 mypy snapshot failure and error was not investigated.
- Exploratory out-of-tree probe of the GC-suspension idea: 10 of 10 pass on 3.11, 5 of 5 on 3.12; overhead within noise on a tiny workload only (about 3.4 s vs 3.5 s); not measured on call-heavy suites.
- Independent reproduction by a separate reviewer matched: 3.11 crashed 5 of 5, 3.12 passed 3 of 3, probe passed 3 of 3 (see the evidence README). The baseline suite and the 3.6.0 control were not re-run by the reviewer.
- No fix was implemented and nothing was posted upstream. The only code written is an out-of-tree, exploratory probe used to test the hypothesis (not a proposed patch).
- Recommendation: **GO to the next owner decision** (maintainer alignment and approval), not to implementation by default. The GC-suspension approach looks more promising than excluding `__del__`; both are hypotheses.
- Limits: one platform that differs from the report, one repro project, Python 3.10 untested, no real-world suite, probe not tested under threads.

## Local implementation phase (2026-11-06; code is NOT published here)
Owner decision: GO to maintainer alignment preparation and a bounded local implementation. Upstream re-checked
2026-11-06: issue unchanged, no competing PR, upstream main still `857019a`. No remote exists on the local checkout.

**Key finding that changes the hypothesis.** The issue describes the cause as a re-entrant `ContextVar.set()`. In our runs
(macOS arm64, 3.11.16) skipping only a nested `set()` still crashed (5 of 5), and guarding only a nested `get()` also
crashed (5 of 5). Guarding both, via a per-thread flag set while `set()`/`reset()` runs, passed 20 of 20. So the working rule is:
a finalizer that interrupts a ContextVar update must not touch the variable at all. This is an observation, not a proof of the CPython root cause.

**Candidates compared (same end-to-end scenarios, 3.11):**
| Candidate | Fixes repro | Notes |
|---|---|---|
| B: per-thread re-entrancy guard (selected for evaluation) | yes | No global GC state. Finalizers interrupting an update are untracked. Micro +350 ns per tracked call; end to end within noise (+6%, large run-to-run spread) |
| A1: GC disable around set/reset (as proposed in the issue) | yes | Demonstrable thread race: GC re-enabled while another thread is still inside `set()` |
| A2: reference-counted, locked GC suspension | yes | Closes the race, but process-wide GC state; micro +1.1 us per call, end to end about +24% |
| C: skip tracking inside `__del__` | partial | Fails 3 of 3 when the finalizer calls another trampolined function |

**Tests (candidate B, local):** unit tests for guard behavior, exception paths, per-thread scope, GC state untouched, and
the `reset()` branch; end-to-end subprocess regression for the original reproducer plus a finalizer-calls-helper case
(both exit -11 on the unmodified base, pass on the candidate); a multithreaded case that does NOT fail on the base and is
only a non-regression check. 14 new tests pass on 3.10, 3.11 and 3.12. Full suite: no failures attributable to the change; the only
failure seen anywhere is `test_setproctitle_crashes_after_fork_with_corefoundation_loaded`, which fails about half the time on the unmodified base (macOS, unrelated).

**Review:** independent exact-SHA review of the candidate found no correctness bugs and called it defensible as a mitigation,
requesting softer root-cause wording and a test for the `reset()` branch (both done). QE Gate was run as advisory evidence only:
risk MEDIUM, `core.py` coverage 92.5%, test and coverage artifacts marked UNTRUSTED because no producer provenance was recorded.

**Unresolved risks:** root cause in CPython not independently confirmed; the `< 3.12` gate is an estimate; one platform
(macOS arm64) differing from the reporter's; a finalizer that interrupts an update gets a "no caller" dependency edge
recorded (imprecise, harmless); `get()` itself being interrupted is assumed safe; maintainers may prefer another approach; overhead measured
on small workloads only.

**Recommendation:** GO to owner-led maintainer alignment. No PR until the owner approves submission.

## Pointers
Executive report section 2.1 C1 and section 3 recommendation 1; ledger section 2.
