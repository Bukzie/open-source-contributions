# 02 - Software testing, QA, CI and developer tooling: contribution scouting

Date of research: 2026-11-04. Read-only (gh api / gh issue list / gh pr list). Nothing was commented, claimed, forked or created on GitHub.
Raw evidence: `evidence/` (local archive, not published) (issue/PR JSON, CONTRIBUTING copies, issue-detail dumps, PR body dumps, fetched source files).

Labels: VERIFIED = observed in gh output / fetched file on 2026-11-04 (URL or number given). HYPOTHESIS = my inference, not verified.
Limits: merge counts come from `gh pr list --state merged --limit 100` filtered to mergedAt > 2026-08-06 (all lists had fewer than 100 hits in-window, so counts are complete for the window). "PR covers issue" checks were done by grepping the bodies/titles of the latest 100 PRs per repo plus issue timelines; a PR that does not mention the issue number could be missed. `gh api search/issues` returned empty results for every query, so it was not relied on.

## 1. Repos screened

| Repo | Stack / license | Size | Last push | Merged PRs since 2026-08-06 | Verdict |
|---|---|---|---|---|---|
| [boxed/mutmut](https://github.com/boxed/mutmut) | Python, BSD-3-Clause; mutation testing | 1,523 stars, 76 open issues | 2026-10-28 (Release 3.8.1) | 23 | BEST FIT (mid-size, responsive collaborators, real unclaimed bugs) |
| [stryker-mutator/stryker-js](https://github.com/stryker-mutator/stryker-js) | TypeScript monorepo (pnpm), Apache-2.0 | 3,324 stars, 129 open issues | 2026-10-30 | 74 (mostly Renovate; about 13+ human/maintainer PRs) | Possible, but slow community-PR review |
| [HypothesisWorks/hypothesis](https://github.com/HypothesisWorks/hypothesis) | Python, GitHub reports NOASSERTION (HYPOTHESIS: MPL-2.0 for hypothesis-python); property-based testing | 9,132 stars, 52 open issues | 2026-11-03 | 61 | Healthy but every fresh item already has a PR; strict AI policy |
| [nektos/act](https://github.com/nektos/act) | Go, MIT; run GitHub Actions locally | 72,527 stars, 375 open issues | 2026-11-03 | 20 | Rejected: huge PR backlog, every actionable issue already has a PR |

## 2. Per-repo findings

### 2.1 boxed/mutmut

- Purpose/stack: mutation testing for Python; uv, pytest, ruff via pre-commit, inline-snapshot for E2E tests. VERIFIED: [CONTRIBUTING.rst](https://github.com/boxed/mutmut/blob/main/CONTRIBUTING.rst) (`uv sync`, `uv run pytest`, `uv run pre-commit run --all-files`, `./scripts/run_tests.sh` for container runs, `--inline-snapshot=fix` to update snapshots; points to ARCHITECTURE.rst).
- AI policy: VERIFIED none in CONTRIBUTING.rst; no AGENTS.md/CLAUDE.md in root tree; no PR template found under `.github` (only `workflows`). VERIFIED tolerance in practice: [#577](https://github.com/boxed/mutmut/issues/577) body says "AI-drafted, verified by me", [#584](https://github.com/boxed/mutmut/issues/584) says "Posted by Claude on the reporter's behalf"; collaborators answered both. Still, disclose AI use (HYPOTHESIS: safest).
- Responsiveness (VERIFIED, collaborator Otto-AA unless noted): #577 filed 2026-09-09, reply 2026-09-10; #490 filed 2026-04-03, reply 2026-04-04; #555 filed 2026-08-23, reply same day; #529 filed 2026-06-12, reply 2026-06-14; #541 filed 2026-07-29, reply 2026-08-08 (10 days). 23 merges since 2026-08-06; last merge 2026-10-28 (#616). Many issues from the last 3 weeks have 0 comments (e.g. #596, #584, #624, #622, #618), so triage is not instant for everything.
- Competition: VERIFIED 19 open PRs, mostly from the last 5 weeks and most map to an open issue (#625->#624, #623->#387, #621->#601, #619->#618, #617->#597, #607->#344, #606->#602, #595->#582, #594->#592, #591->#590, #589->#583, #587->#586, #580->#439, #579->#577). So most "obvious" issues are taken.
- Unclaimed with no matching PR found: #596, #584, #555, #545, #541, #535, #521, #490. Rejections below.
- Labels: only [#577](https://github.com/boxed/mutmut/issues/577) and [#439](https://github.com/boxed/mutmut/issues/439) carry "good first issue"; both have PRs (#579, #580).

### 2.2 stryker-mutator/stryker-js

- Purpose/stack: mutation testing for JS/TS, plugins for jest/vitest/mocha/karma etc. VERIFIED: [CONTRIBUTING.md](https://github.com/stryker-mutator/stryker-js/blob/master/CONTRIBUTING.md): "create an issue first or let us know via Slack", unit tests required, `pnpm run build`, `pnpm test`, `pnpm run lint`, Angular-style commits (`fix(core): ...`), and "we estimate the response time from the maintainers is around a day or so". No AI policy text found (grep for AI/LLM/copilot/generated returned nothing relevant). VERIFIED context: merged [#6114](https://github.com/stryker-mutator/stryker-js/pull/6114) "add a dev-container for working with sandboxed agents"; a `copilot-swe-agent` draft PR (#6029) exists.
- Responsiveness: CONTRIBUTING claims about a day; evidence contradicts it for community PRs. VERIFIED zero comments and zero reviews as of 2026-11-04 on open PRs #6228 (2026-09-22), #6226 (2026-09-19), #6244 (2026-10-05), #6145 (2026-07-25), #6146 (2026-07-25). #6229 (2026-09-24): a user asked on 2026-10-14 for a maintainer to give it a thumbs up, no reply recorded. #6246: first-time contributor on 2026-10-07 asked for CI approval; approval review from a maintainer-side account only on 2026-10-23 (16 days). 53 open PRs. Maintainer-authored work does merge in bursts (2026-10-23, #6268, #6269, #6246, #6214).
- Issues are plentiful and detailed (many look AI-assisted, VERIFIED e.g. unusual detail in #6295, #6235, #6233) but almost no maintainer (MEMBER) replies; replies come from other users (#6208, #6224, #6213). Only [#4681](https://github.com/stryker-mutator/stryker-js/issues/4681) has "Good first issue" and it is labelled stale (2023).
- Competing PRs (VERIFIED): #6259 for #6257, #6254 for #6253, #6229 for #6224, #6226 probably for #6233 (title "don't throw when an error cannot be coerced to a primitive", HYPOTHESIS that it covers #6233), #6228 for #6208/#6227, #6267 for #6130, #6275 for #6256, #6310 for #6119.

### 2.3 HypothesisWorks/hypothesis

- VERIFIED [CONTRIBUTING.rst](https://github.com/HypothesisWorks/hypothesis/blob/master/CONTRIBUTING.rst) has an explicit "AI Policy": AI use is fine, but every issue/PR/comment must come from a human who has read it fully, takes responsibility, and "clearly mark such content as AI-written"; "We do not allow unreviewed or fully-autonomous contributions". `.claude/` directory (CLAUDE.md, commands, skills) exists in repo. VERIFIED enforcement: a maintainer closed [#4906](https://github.com/HypothesisWorks/hypothesis/pull/4906) on 2026-10-18 pointing to the policy and describing the issue as unsuitable for AI-driven work; another attempt #4837 for the same issue was also closed.
- Responsiveness: 61 merges since 2026-08-06, last 2026-11-03; maintainers (Zac-HD, Liam-DeVoe) engage with PRs within hours (e.g. Zac-HD on #4946 within about 10 hours).
- Competing PRs (VERIFIED): every fresh bug has a PR: #4950->#4951, #4943 and #4881->#4944 and #4884 (two open PRs for the same Ghostwriter bug), #4917->#4919, #4107 (async stateful)->#4953, #4880->#4890 (closed). No "good first issue"/"help wanted" labels exist on any open issue (VERIFIED label list).
- Remaining open issues are design-heavy: #4170 (maintainers floated replacing `st.data()` with a callable `st.draw()`, design unresolved; a newcomer expressed interest on 2026-10-24, unanswered), #4132 (subtle, AI attempts rejected), #4572 (blocked on setuptools#5112), #4089 (prior PR #4872 closed).

### 2.4 nektos/act

- VERIFIED [CONTRIBUTING.md](https://github.com/nektos/act/blob/master/CONTRIBUTING.md): link the issue (`fixes #N`), `golangci-lint`, tests; [AGENTS.md](https://github.com/nektos/act/blob/master/AGENTS.md) exists (commands `make test-fast`, `make pr`, layout, lint rules); [PR template](https://github.com/nektos/act/blob/master/.github/pull_request_template.md) checklist: linked issue, tests or explanation, description. No explicit AI disclosure rule seen in the portions I read (HYPOTHESIS: none).
- Responsiveness: 20 merges since 2026-08-06, most on 2026-10-28 to 2026-10-31 (maintainer sweep: CI hardening, branch rename master->main, artifact-server hardening). VERIFIED 40+ community PRs open with last-update 2026-10-28 and many created June to September with no reviews; recent issues mostly 0 comments (e.g. #6236, #6233, #6173). 97 of 100 bug issues carry the stale label.
- Competition (VERIFIED): #6236->#6237, #6194->#6203, #6195->#6198, #6181->#6197, #6189->#6193, #6180->#6186 (contributor said "I'll take this one" on 2026-10-07), #6131->#6132, #6159->#6164, #6166->#6167, #6171->#6172, #6124->#6161, #6173/#6114->#6174. Unclaimed ones left are vague (#6178 "tsc build exits 1", #6120 "speed up"), or a minor UX item (#6121).
- Rejected as a target: low review throughput, crowded, 72k-star project where a newcomer is not likely to be noticed.

## 3. Proposals (4)

### P1. mutmut #596: segfault in stats collection on Python 3.11 when a trampolined `__del__` runs during GC

- Issue: [boxed/mutmut#596](https://github.com/boxed/mutmut/issues/596) (opened 2026-10-11 by yeongseon; 0 comments; no label; no assignee; VERIFIED no PR found referencing it or its cause terms in the latest 100 PRs).
- Problem and users: VERIFIED per the issue: since #509 (3.7.0) the stats-mode trampoline calls `MutmutCallStack.set()/reset()` (a ContextVar) on every trampolined call, and `__del__` methods are trampolined. On CPython 3.11 and earlier the cyclic GC can run inside `ContextVar.set()` and re-enter it, a CPython use-after-free (python/cpython#148891, fix python/cpython#148928 per the issue). Result: exit 139 / `TypeError: can't concat int to bytes` / `failed to collect stats`. Python 3.10/3.11 users with classes that have `__del__` cannot run mutmut 3.7+ at all; the reporter's project pinned to 3.12+ as a workaround. The issue has a minimal 3-file repro.
- Why it matters: hard crash with no workaround for supported Pythons (CI covers 3.10 to 3.14 per Otto-AA's comment on #490, VERIFIED).
- Proposed solution (from the issue, "verified" there): on `sys.version_info < (3, 12)`, disable the GC around `MutmutCallStack.set`/`reset` and restore previous state (`gc.isenabled()` check, try/finally). Alternative: skip ContextVar tracking inside `__del__`.
- Files: `src/mutmut/core.py` (VERIFIED `MutmutCallStack` with `set`/`reset` classmethods); callers in `src/mutmut/mutation/trampoline.py` lines 94-102 (VERIFIED). Tests: `tests/mutation/test_trampoline.py`.
- Tests / acceptance: a unit test that `set`/`reset` restore the previous GC state (including when GC was already disabled and when reset raises); a version-gated regression test (skip on >= 3.12) that runs the issue's repro through stats collection; ruff/pre-commit and `uv run pytest` green; the repro from #596 exits 0 on 3.11.
- Effort: 0.5 to 1 day (the hard part is a reliable 3.11 CI/local repro; GC timing is non-deterministic, use the 200k-iteration loop from the issue).
- Risks: perf overhead of `gc.disable/enable` on every call (HYPOTHESIS: small but measure); thread-safety of toggling global GC state across threads/async (HYPOTHESIS: use a re-entrancy-safe save/restore, or only toggle inside stats mode); need Python 3.11 in the dev env.
- Acceptance likelihood: HYPOTHESIS medium-high (about 65-75%). Justification: crash bug with repro and a proposed fix, collaborators (Otto-AA, nicklafleur) respond within 1 to 2 days on most issues (VERIFIED above) and 23 PRs merged in 90 days; risk is a competing PR landing first (19 open PRs show an active contributor crowd) and maintainers preferring the "skip `__del__`" approach.
- Maintainer discussion first: yes, a short comment on #596 stating intent and the chosen approach (avoid duplicate work given the crowd).

### P2. mutmut #584: test-spawned process pools outlive every mutant (process group cleanup)

- Issue: [boxed/mutmut#584](https://github.com/boxed/mutmut/issues/584) (2026-09-24, m-groom, 0 comments, no PR found). Soft-claim risk: reporter wrote "Happy to share it or open a PR for the fix above if that would help" (VERIFIED), no PR in 6 weeks.
- Problem: VERIFIED per issue: joblib/loky, `multiprocessing.Pool`, `ProcessPoolExecutor` children survive mutant runs because forked test runs end with `os._exit()` (skipping atexit shutdown) and share mutmut's process group; reporter saw 8,359 orphaned processes and 120 GB RAM exhausted on a 15,800-mutant run; reproduces on Linux and macOS with a 3-file repro.
- Proposed solution (from the issue): `os.setpgid(0, 0)` in the child right after each fork; after reaping, `os.killpg(pid, SIGTERM)` (optional SIGKILL after grace), ignore `ProcessLookupError`; on timeout signal the group (`os.killpg`) rather than the PID.
- Files (VERIFIED line refs match the fetched source): `src/mutmut/workers/isolation.py` (fork sites at lines 85, 142, 396, 577, 853; `os._exit` at 595, 871), `src/mutmut/workers/timeout.py` line 53 (`os.kill(pid, signal.SIGXCPU)`). Tests: `tests/workers/test_isolation.py`, `tests/workers/test_timeout.py`.
- Tests / acceptance: test that a mutant test spawning a child process leaves zero surviving processes after the run (POSIX only, skip on Windows); timeout still produces the same verdict; existing E2E snapshots unchanged.
- Effort: 1 to 2 days (POSIX semantics, macOS vs Linux, forkserver and fork modes, both paths).
- Risks: killing the group could kill unrelated processes if `setpgid` is not applied before `killpg` (race; HYPOTHESIS); interaction with the recent "process isolation" feature (#566 merged 2026-09-12); a terminal-controlling process group nuance; Windows branch must be untouched.
- Acceptance likelihood: HYPOTHESIS medium (about 50-60%). Justification: real, measured impact and clear design, but touches the core isolation code of a feature merged 7 weeks ago, so reviewers will be cautious, and the reporter may still submit.
- Maintainer discussion first: yes. Ask on #584 whether the reporter is already working on it; offer to take it if not.

### P3. stryker-js #6235: `TSConfigPreprocessor` ignores `extends` arrays and assumes a one-segment `tempDirName`

- Issue: [stryker-mutator/stryker-js#6235](https://github.com/stryker-mutator/stryker-js/issues/6235) (2026-09-29; 1 user comment 2026-10-15 describing a related variant; no maintainer reply; no PR referencing it found).
- Problem: VERIFIED in fetched `packages/core/src/sandbox/ts-config-preprocessor.ts` on master: the config type declares `extends?: string;` (line 13), so a TS 5+ `extends` array is not rewritten and escapes the sandbox; per issue, rewrites prepend exactly `../../` which is wrong when `tempDirName` is nested or placed outside the project. Affects monorepos using shared base tsconfigs with array extends (increasingly common) and custom `tempDirName`.
- Proposed solution: handle `string | string[]` in `rewriteExtends`; compute the relative prefix from the actual sandbox path to the project root instead of hard-coding `../../`; unit tests in the existing spec.
- Files: `packages/core/src/sandbox/ts-config-preprocessor.ts`, `packages/core/test/unit/sandbox/ts-config-preprocessor.spec.ts`.
- Tests / acceptance: spec cases for `extends: [a, b]`, nested `tempDirName`, `tempDirName` outside project; `pnpm test` and `pnpm run lint` pass; fix(core) commit style.
- Effort: 1 day.
- Risks: HIGH conflict risk: open PR [#6231](https://github.com/stryker-mutator/stryker-js/pull/6231) (updated 2026-11-02, TypeScript 7 support) rewrites the same file and its spec (VERIFIED file list: `ts-config-preprocessor.ts`, `ts-config-preprocessor.spec.ts`). Should wait for it to merge or base on it. Maintainers are slow on community PRs (section 2.2), so the PR may sit for weeks.
- Acceptance likelihood: HYPOTHESIS low-medium (about 35-45%): sound fix, but unreviewed-PR backlog and file overlap.
- Maintainer discussion first: yes; comment on #6235 and on #6231's author, and wait for #6231 to land.

### P4 (small, optional). stryker-js #6005: `stryker init` should add `reports/` to `.gitignore`

- Issue: [#6005](https://github.com/stryker-mutator/stryker-js/issues/6005) (2026-05-16, 1 non-maintainer comment suggesting a nested `.gitignore` inside `.stryker-tmp` instead). No maintainer response in 5+ months (VERIFIED). A prior PR [#6016](https://github.com/stryker-mutator/stryker-js/pull/6016) by `ai-agent-lead` "add reports/ to .gitignore template" was closed 2026-06-21 with no comment (VERIFIED); reason unknown.
- Proposed solution: extend `GitignoreWriter.addStrykerTempFolder` to also append `reports` (check each entry individually; fix the existing `includes()` substring check). VERIFIED current code only checks/appends `defaultOptions.tempDirName`.
- Files: `packages/core/src/initializer/gitignore-writer.ts`, `packages/core/test/unit/initializer/gitignore-writer.spec.ts`.
- Effort: 1 to 2 hours. Risks: scope is a UX choice (reports dir name is configurable; maintainers may not want it); substring `includes` bug could mis-skip. Acceptance likelihood: HYPOTHESIS low-medium (30-40%) given no maintainer opinion and a prior closed PR. Needs a maintainer thumbs-up on the issue first. Low value alone; useful only as a first-PR warm-up.

## 4. Rejections

| Item | Reason |
|---|---|
| mutmut #577 (case-flip mutations, "good first issue") | VERIFIED claimed: nabi-noor commented 2026-09-10 with a design; open PR #579 (and #580 for #439). |
| mutmut #529 (copy lockfiles) | PR #534 by the reporter was opened 2026-06-28 and is closed (VERIFIED closed; merge status unconfirmed). Maintainers want git-tracked-file copying; unclear state. |
| mutmut #490 (race in `inner_timout_checker`) | Collaborator says likely fixed by #410 in newer version; stale, needs retest (VERIFIED comment 2026-04-04). |
| mutmut #555 (`mutate_only_covered_lines` stale line numbers) | Collaborator has no solution; requires redesign of coverage runs (VERIFIED comment); high effort, needs maintainer design input. |
| mutmut #545 (timeout budget parallelism-blind) | Speculative multi-option design, overlaps closed #492 / PR #493; changes scoring semantics. |
| mutmut #541 (type-checker "Could not find mutant") | Disagreement between reporter and collaborator on approach (VERIFIED thread); maintainers hold the design. |
| mutmut #602, #601, #597, #592, #590, #586, #583, #582, #618, #601 | Each has an open PR (see 2.1). |
| stryker #6233 | Probably covered by open PR #6226 (HYPOTHESIS from title); stryker #6208 is "maintainer decision" per a commenter (existing test pins behavior) and has PR #6228. |
| stryker #6295 (Windows hang in LoggingServer) | Needs Windows to reproduce; no maintainer input; high risk of unreviewed PR. Worth watching, not proposing. |
| stryker #5849 (`STRYKER_CONFIG_PATH`) | Maintainer (jaspervdveen) questioned the benefit on 2026-02-27; no approval. |
| stryker #6222, #6176 | Dependency/engine housekeeping; #6176 has PR #6177. |
| Hypothesis #4950, #4943, #4881, #4917, #4107, #4880 | All have open/closed PRs (#4951, #4944 and #4884, #4919, #4953, #4890). |
| Hypothesis #4132 | Maintainers closed two AI-driven PRs; high bar. |
| Hypothesis #4170 | API design unsettled (callable `st.draw()` idea); another user already asked to work on it; docs-only slice is likely to be redone. |
| Hypothesis #4572 | Blocked on setuptools#5112. |
| Hypothesis #4089 | Prior PR #4872 closed; design-heavy. |
| act: nearly all recent issues (#6236, #6194, #6195, #6189, #6180, #6181, #6131, #6159, #6166, #6171, #6124, #6173) | Open PRs exist for each (see 2.4); #6180 explicitly claimed by JasonMetal. |
| act #6121 (docker config.json handling) | Minor, no maintainer interest recorded, low value. |
| act #6178, #6120 | Vague, not reproducible from the issue text. |

## 5. Ranking and recommendation

1. P1 (mutmut #596): best value/risk: clear crash, tiny code change, responsive collaborators.
2. P2 (mutmut #584): higher impact, higher risk; check with reporter first.
3. P3 (stryker #6235) only after #6231 merges.
4. P4 only as a warm-up with prior maintainer ack.

Caveat: mutmut's contributor crowd is large and recent (19 open PRs, several from first-time contributors in the last 5 weeks), so move quickly on P1/P2 and re-check for new PRs immediately before starting.
