# mutmut #596 validation evidence (2026-11-05)

Read-only validation. No upstream file was modified (`git status` clean in the clone before and after). Nothing was
posted upstream. Raw outputs have home and temp paths replaced with placeholders such as `<repo>` and `<tmp>` (a second scrub pass was needed after review).

## Subject
- Issue: https://github.com/boxed/mutmut/issues/596 (state OPEN, 0 comments, no assignee, no labels, last updated 2026-10-11T01:02:35Z; checked 2026-11-05)
- Upstream clone: `boxed/mutmut` at `857019a67cffddf0fb8a294247e9a147722d3001` (commit 2026-10-28, "chore(deps): bump virtualenv ... (#613)"), mutmut 3.8.1
- Competing work (checked 2026-11-05): 19 open PRs, none about GC, `ContextVar`, `__del__`, segfault or #596 (nearest by title: #619 macOS proxy before forking, #621 exception reported as killed). The issue timeline shows only the reporter's own downstream cross-references. PR search for these terms returned nothing.
- Contribution rules: `CONTRIBUTING.rst` only; no AI policy text in it or the README; no `AGENTS.md`, `CLAUDE.md`, `AI_POLICY.md` or PR template present.

## Platform and versions
macOS (Darwin, arm64). The reporter used Linux x86_64; this is a different platform.
CPython 3.11.16 and 3.12.13 (uv-managed). mutmut 3.8.1 built from the clone (non-editable). pytest 9.2.0, libcst 1.9.0.
Regression control: mutmut 3.6.0 with pytest 8.4.2 on 3.11.16.

## Reproduction commands
```sh
uv venv --python 3.11 venvs/py311 && uv pip install --python venvs/py311/bin/python ./mutmut pytest
uv venv --python 3.12 venvs/py312 && uv pip install --python venvs/py312/bin/python ./mutmut pytest
# project files are in repro/ (copied from the issue body unchanged)
python3 run_repro.py <abs path to venv python> <abs path to project dir> <runs> <timeout seconds>
```
`run_repro.py` runs `python -m mutmut run` per trial in a fresh copy, new process group, core dumps off, CPU limit,
wall-clock timeout with group kill. No memory limit (not enforceable on macOS).

## Results (return code per trial)
| Configuration | Trials | Outcomes |
|---|---|---|
| 3.11.16, mutmut 3.8.1 | 10 | 10 x -11 (SIGSEGV), about 0.4 s each |
| 3.12.13, mutmut 3.8.1 (control) | 5 | 5 x 0 |
| 3.11.16, mutmut 3.6.0, pytest 8.4.2 (regression control) | 3 | 3 x 0 |
| 3.11.16, mutmut 3.6.0, pytest 9.2.0 | 3 | 3 x 1: INVALID control, unrelated plugin error with pytest 9.2 (`_nodeid`); kept for transparency |
| 3.11.16, mutmut 3.8.1 + exploratory probe H1 | 10 | 10 x 0 |
| 3.12.13, mutmut 3.8.1 + probe H1 | 5 | 5 x 0 |

No intermittency was observed: the crash was deterministic on this platform for this repro. The top crash frame
(`crash-trace-py311-mutmut-3.8.1.txt`) is `stats.py:173 record_trampoline_hit` called from the stats-mode trampoline,
consistent with the issue. The trace alone does not prove the CPython root cause cited in the issue; the 3.12
control, the 3.6.0 control and the probe result are consistent with it.

## Baseline tests (upstream suite, unmodified, `uv run --frozen`, environment outside the clone)
- 3.12: 473 passed, 2 failed, 2 skipped. Failures: pyrefly snapshot (`cannot identify current dir`), setproctitle test ("library may have been fixed").
- 3.11: 472 passed, 3 failed, 1 error, 2 skipped. Same two failures plus a mypy type-checking snapshot failure and error.
  The mypy snapshot difference was not investigated; nothing observed ties any failure to this issue.
See `baseline-py311-summary.txt`, `baseline-py312-summary.txt`.

## Exploratory probe (hypothesis H1, not a fix)
`probe-gc-suspension/sitecustomize.py`, activated with `MUTMUT_596_PROBE=1` and `PYTHONPATH`, wraps `MutmutCallStack.set`
and `reset` to disable the cyclic GC around the call and restore the prior state. Out of tree; upstream untouched.
Timing, 3.12 (5 trials each, median): unpatched 3.4 s and 3.7 s in two batches, patched 3.5 s. Overhead is within noise for this
workload; it says nothing about call-heavy real suites.
(The harness interpreter printed `No module named 'mutmut'` from the probe because it also inherited `PYTHONPATH`; harmless.)

## Limitations
Single platform that differs from the report; one reproduction project; 10 and 5 trial counts; Python 3.10 not tested;
no real-world codebase; thread-safety of the probe not tested; overhead only measured on a tiny workload.

## Fresh-check source
Upstream state claims above (issue state, open PRs, PR keyword searches, absent policy files, timeline) are backed by
`fresh-upstream-checks.txt`, captured read-only on 2026-11-05 after the main run.

## Independent verification (2026-11-05)
A separate reviewer who did not run the work rebuilt fresh Python 3.11.16 and 3.12.13 environments (mutmut 3.8.1,
pytest 9.2.0, libcst 1.9.0) and re-ran the harness against commit `1ce31b6` of this repository (content later
republished with the changes listed below). Observed: clone HEAD `857019a` with a clean tree and an unchanged upstream tip
(`git ls-remote`); reproduction project identical to the issue body; 3.11: 5 of 5 trials SIGSEGV (-11); 3.12: 3 of 3
exit 0; probe on 3.11: 3 of 3 exit 0. Result tables and baseline summaries were checked for consistency with the raw files.
Not independently re-run: the full baseline suite and the mutmut 3.6.0 control.
Changes made after that review: two tracked `.pyc` files that embedded a local path were removed and `__pycache__` is
now ignored; this section, `fresh-upstream-checks.txt` and wording qualifiers were added.
