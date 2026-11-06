# Validation mission: boxed/mutmut #596

**Scope: VALIDATE only. Read-only toward GitHub and toward upstream source. No fix, fork, comment, PR or merge.**
Authorized by the owner on 2026-11-05. Workflow V2. QE Gate is not required because no code is produced.

## Outcome
A dated, evidence-backed VALIDATE record that states whether the crash reproduces, under what conditions, and
whether work should proceed, with a GO, HOLD or STOP recommendation. Any proposed fix is a hypothesis.

## Acceptance criteria
1. Fresh upstream checks are recorded with the time they were made.
2. The exact upstream SHA, interpreter and dependency versions, and every command are recorded.
3. The reported crash is run on Python 3.11 several times, and outcomes are reported as observed, including
   intermittent behavior. Exit code 139 is not assumed.
4. Python 3.12 is run as a control, and an older mutmut release is run as a regression control.
5. The upstream test suite is run unmodified as a baseline.
6. The relevant implementation is read without modifying any upstream file.
7. A separate reviewer reproduces the findings and checks the evidence against the recorded SHA.
8. Candidate record, tracking index and Project status are updated to Validation.

## Steps
1. **Fresh upstream checks (read-only `gh`)**: issue state, assignee, comments, timeline cross-references; open
   and recently merged PRs; keyword search for GC, `ContextVar`, `__del__`, segfault; CONTRIBUTING and any AI
   policy file (AGENTS.md, CLAUDE.md, AI_POLICY.md, PR template).
2. **Clone** upstream into the git-ignored `workspaces/`. Record `git rev-parse HEAD`. Confirm the clone stays
   clean (`git status`) at the end.
3. **Environments**: separate virtual environments outside the clone for Python 3.11, Python 3.12, and a
   regression control (mutmut 3.6.0 with a compatible older pytest). Record interpreter, platform and package
   versions.
4. **Reproduction**: the three-file project from the issue, run through an isolated subprocess harness with a new
   process group, wall-clock timeout, CPU-time limit, core dumps disabled and a fresh copy of the project per run.
   Memory limits are not reliably enforceable on macOS and must be reported as a limitation. Run 10 trials on 3.11,
   5 on 3.12, 3 on the regression control. Record return code, signal, duration and output tail for each.
5. **Baseline tests**: run the upstream suite unmodified on 3.11 and 3.12 with an environment outside the clone.
   Record failures and whether any relate to the crash.
6. **Implementation inspection**: `MutmutCallStack` in `core.py`, stats-mode trampoline, and the stats recording
   path. Compare the GC-suspension and `__del__`-exclusion hypotheses by reading; any out-of-tree probe must be
   labeled exploratory and must not modify upstream files.
7. **Independent verification**: a reviewer who did not run the work re-creates the environments from the written
   commands, re-runs the reproduction, and checks the recorded SHA and evidence files.
8. **Records**: dated evidence under `candidates/evidence/mutmut-596/<date>/` (paths scrubbed), update
   `candidates/active/01-mutmut-596.md` and `tracking/CONTRIBUTION_INDEX.md`, move the Project item to
   Validation. Do not advance beyond VALIDATE.

## Exclusions
No fork, branch, push, comment, reaction, issue claim or PR upstream. No edits to upstream files. Posting
anything upstream is the owner's decision and the owner's words.

## Known limitations to report
- Reproduction platform may differ from the reporter's (the issue used Linux x86_64).
- A GC-timing bug can be intermittent; N trials are evidence, not proof of probability.
- Memory limits cannot be enforced on macOS.

## Exit
The owner decides: proceed to MAINTAINER ALIGNMENT or OWNER APPROVAL for implementation, hold, or stop.
