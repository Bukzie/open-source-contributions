# Recommended first validation mission: boxed/mutmut #596

**Status: proposal only. Requires owner approval to start. Does not include implementation.**

## Outcome
A written VALIDATE record for mutmut #596 that says whether the problem reproduces and whether the work is still
unclaimed.

## Steps (all read-only toward GitHub)
1. Fresh check of https://github.com/boxed/mutmut/issues/596 and the open PR list: comments, assignee, any PR
   mentioning GC, `ContextVar`, `__del__` or #596.
2. Re-read mutmut's CONTRIBUTING and look for any AI policy added since 2026-11-04.
3. Clone upstream into `workspaces/` (read only; no fork yet). Create a Python 3.11 environment.
4. Reproduce the crash with the three-file repro from the issue. Capture output and exit code.
5. Confirm the code positions in `src/mutmut/core.py` and `src/mutmut/mutation/trampoline.py` on current main.
6. Write findings into `candidates/active/01-mutmut-596.md` and `tracking/CONTRIBUTION_INDEX.md`.

## Exclusions
No fork, branch, comment, or PR. No code changes. Posting a comment on the issue is the owner's decision and the
owner's words.

## Exit
Owner decides: proceed to MAINTAINER ALIGNMENT / OWNER APPROVAL for implementation, or stop.
