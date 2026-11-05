# 03 AI Verification, Evaluation and Reliability: contribution scouting

Date of research: 2026-11-04. Read-only (gh CLI listing/viewing only). Raw output: `evidence/` (local archive, not published).
Labels: VERIFIED = seen in gh output with the cited number/date. HYPOTHESIS = my inference. I did not run any repro locally, so "repro" below means the repro published in the issue, which I read but did not execute.

## Bottom line

All four repos screened are heavily crowded by (often AI-assisted) drive-by PRs. Nearly every well-reproduced bug already has an open PR within hours or days. The only candidates with real room are the ones where the maintainers have stated a design opinion and no one has implemented it (garak #2339), or a freshly filed repro with no PR (Guardrails #1692). The best newcomer strategy is: pick work the maintainers already described, write the discussion comment first, and be disciplined about duplicate checks.

## Screening table

| Repo | License / stack | Stars / open issues / open PRs | Last push | Merged PRs, last 90 d (since 2026-08-06) | AI policy |
|---|---|---|---|---|---|
| promptfoo/promptfoo | MIT, TypeScript | 26811 / 914 / 758 | 2026-11-04 | at least 1000 (query cap hit) | AGENTS.md exists, no AI-contribution restrictions found (see below) |
| UKGovernmentBEIS/inspect_ai | MIT, Python | 3166 / 494 / 132 | 2026-11-04 | 832 | Explicit, strict (issue-first, AI disclosure) |
| NVIDIA/garak | Apache-2.0, Python | 9852 / 544 / 245 | 2026-11-02 | 67 | Explicit AGENTS.md policy |
| guardrails-ai/guardrails | Apache-2.0, Python | 7583 / 62 / 45 | 2026-11-03 | 5 (all by maintainers) | None found |

All VERIFIED via `gh api repos/...` and `gh pr list --search "merged:>2026-08-06"` on 2026-11-04. Also glanced at: confident-ai/deepeval (19281 stars, 475 open PRs, 77 merged in 90 d; old "help wanted" items from 2023-2025 only: rejected as low-signal), EleutherAI/lm-evaluation-harness (last push 2026-09-14, 614 open PRs, GFI labels all 2021-2025: rejected as stale), explodinggradients/ragas (now vibrantlabsai/ragas, last push 2026-02-24: stale).

---

## 1. UKGovernmentBEIS/inspect_ai (Inspect AI)

Purpose: LLM evaluation framework from the UK AI Security Institute (tasks, solvers, scorers, agent bridges, log viewer). VERIFIED repo metadata.

Contribution rules (VERIFIED, `CONTRIBUTING.md`, `AGENTS.md`, `.github/pull_request_template.md`, saved in evidence):
- Non-roster contributors may only open PRs against an issue a maintainer labelled `accepted`; unlinked PRs are auto-closed by a gate bot (PR #5280 was closed this way, see below). `good first issue` implies `accepted`.
- Duplicates are closed in favour of the earlier PR. 60-day inactivity auto-close. Issues labelled `deferred` cannot take PRs.
- AI use is welcome but must be disclosed in the PR, with an `### Agent review` section (tool, reviewer model, number of fresh-context passes, findings). Contributor must be able to defend every line. Conventional Commits PR titles; do not edit CHANGELOG.md; `uv sync`, `make check`, `make test`.
- Suggests building scorers/providers/tools as extensions rather than in core.

Activity (VERIFIED): 300 merged PRs between 2026-10-04 and 2026-11-03 (`inspect-merged300.json`), mostly by staff (ransomr 80, brandly 52, dragonstyle 48, epatey 23), plus about 40 distinct external authors with 1-4 merges each. Staff PRs merge in hours; external PRs wait longer (e.g. #5700 opened 2026-10-05 still open with 4 reviews). Maintainers triage issues to `accepted` quickly (many accepted within days).

Open `accepted` backlog: 54 issues (`inspect-accepted.json`). I checked every `good first issue` and about 45 other accepted issues for PRs referencing them:
- All 7 open good-first-issues are contested. Examples: #6066 and #5928 (numeric match on CJK units) have PRs #6208 and #6179 (#6105 closed); #6015 has PR #6186; #5980 has PR #6185; #5815 has PR #6156; #5809 has PR #5911; #6094 reporter has a PR ready.
- Nearly every other accepted issue has an open PR. Issues with no PR but taken in comments: #6104 (tim-hua-01 claimed 2026-11-01, actively working), #6052 and #6051 (reporter yinli-systems has fix commits ready, per Cross2pro's withdrawal comments of 2026-10-31).
- Issues without an open PR but not good targets: #5207 (Tinker model provider; policy says use extension), #4193 (`deferred`), #5400 (PR #5401 exists), #4763 (fixed upstream in ts-mono, shipped since 0.3.261 per comment 2026-09-18).

Notable: the bot-gate closed PR #5280 (hf_dataset retry, #5279) on 2026-10-17 because the description lacked a recognised closing keyword; the author says GitHub blocked reopening. (VERIFIED, PR #5280 comments.) A lesson: use `Fixes #NNN` exactly.

Proposals: none recommended for code right now. HYPOTHESIS: the realistic newcomer path is (a) reviewing others' open PRs (CONTRIBUTING.md says feedback on PRs is welcome) and (b) filing high-evidence issues, then waiting for `accepted`. Expect competition from several agents per issue within a day.

---

## 2. promptfoo/promptfoo

Purpose: LLM eval and red-team CLI/library (TypeScript, Node, React web UI, Python/Ruby providers). VERIFIED.

Contribution rules (VERIFIED): `CONTRIBUTING.md` redirects to `site/docs/contributing.md`; `AGENTS.md` (22 KB) is operational guidance for agents (branch workflow, tests, no direct commits to main). No PR template found (`.github/pull_request_template.md` 404). No formal AI-disclosure rule found in these files (grep for AI policy turned up none; not proven absent elsewhere). Docs say "talk to us first" if unsure about acceptance (`site/docs/contributing.md` line 133). Labels `good-first-issue` and `help-wanted` exist but 0 open issues carry them (VERIFIED `gh issue list -l`). Issues are not labelled by maintainers (all 40 sampled recent issues have empty labels).

Activity (VERIFIED, `promptfoo-merged150.json`): at least 1000 merges in 90 days; 150 most recent merged between 2026-10-13 and 2026-11-03. Maintainers appear as `-oai` accounts (mldangelo-oai, ianw-oai, alandelong-oai); HYPOTHESIS: the project is now OpenAI-affiliated. They do merge external fixes quickly, e.g. #12054 and #12025 (Shaurya55555) in 3h and 34h, #11957 (no-hup) after 151h, #11881 and #11878 (fallintoplace) after about 300h.

Crowding (VERIFIED): for the 14 recent bug issues I checked, 11 already have 1-2 open PRs (#11883 -> #11885; #11779 -> #11780; #11857 -> #11858; #11775 -> #11776; #11937 -> #11947; #12061 -> #12062 and #12084; #11773 -> #11774; #12093 -> #12094; #12077 -> #12078, #12079; #12004 -> #12005; #11928 -> #11930; #11927 -> #11929; #11922 -> #11926; #11921 -> #11924, #11966; #11918 -> #11925).

Rejections: 
- #11041 (isEmptyResponse treats 'undefined'/'null' as refusal): two prior PRs (#11050, #11274) closed; maintainer mldangelo wrote on #11274 that empty/undefined/null counting as refusals is intentional (#5431, #10621). Policy question, not a bug.
- #11057 (copy working_dir per call): largely delivered by merged #11063 "run coding agents in isolated copy_working_dir workspaces". Duplicate.
- #11487 (`not-is-valid-openai-tools-call` ignores `not-`): clear repro, no PR in 26 days, but original author said on 2026-10-08 "I have a small fix with tests ready" and oliarmak-web asked to take it 2026-10-15. Claimed twice. Could be revisited if both go silent; HYPOTHESIS only.
- #12116 (Python/Ruby providers await cache.set, 200+ ms with large cache.json): filed 2026-11-03, author is holding a PR pending maintainer direction and flags conflicting #11198. Not mine to take.
- #11305 (OR values in --filter-metadata): PR #11320 merged.
- New-provider/plugin/example/probe proposals (#11954, #11946, #11474, #11821, #11818, #11902): speculative or promotional, gated by the provider bar in docs.

Proposals: none recommended. HYPOTHESIS: the only way to land here is to be first on a freshly filed bug (hours, not days), which is a race against several accounts.

---

## 3. NVIDIA/garak (mid-sized, newcomers are being merged)

Purpose: LLM vulnerability scanner / red-teaming toolkit (Python; probes, detectors, generators, buffs). VERIFIED.

Contribution rules (VERIFIED, `garak-AGENTS.md`, `garak-CONTRIBUTING.md`, `garak-PR-template.md`):
- AGENTS.md: applies to all AI-assisted contributions, "breaching can result in automatic banning". No pure code-agent PRs; human must review every line; PR description must state why it is not a duplicate, list test commands and results, and state that AI assistance was used. Add attribution via commit trailer. No issue numbers in PR titles (fine in body). No single-typo busywork PRs. Avoid issues labelled `needs-triage` unless a maintainer replies first; avoid unassigned bugs lacking `bug-verified` unless you have a working test; avoid `needs-*` labels.
- PR template wants verification steps and `python -m pytest tests/`. Default branch is `main`.
- Bug issues are meant to go `needs-repro` -> `needs-fix`; contributions via `docs/source/contributing.rst`.

Activity (VERIFIED): 67 merged PRs since 2026-08-06; the last 100 merged PRs (2026-06-09 to 2026-10-27) come from about 50 distinct authors, so first-timers do get merged (anxkhn 7, patriciapampanelli 11, jmartin-tech 11, WatchTree-19 4, feiiiiii5 4). Maintainer jmartin-tech (COLLABORATOR) answered #2339 the same day it was filed (2026-10-20). Triage backlog is large: about 40 open issues carry `needs-triage`, most filed October 2026, and few have PRs from non-bot accounts that were invited.

Maintainer-invited work: old `good first issue` items (probes #1349, #841, #683, #515, #456 etc.) are 1-3 years old, maintainers have never assigned them, and each is a new probe needing scope review. HYPOTHESIS: new-probe PRs are the likeliest to be accepted but also slowest to review; they were out of scope for this bug-focused screen.

Rejections:
- #1919 (AgentBreaker mis-tagged OWASP llm07/08): `bug-verified`, but 5 PRs (#1920, #2072, #2073, #2277, #2283) are all CLOSED. Maintainers (jmartin-tech 2026-07-07, leondz 2026-08-13) want a catalogue-wide decision on OWASP tag versioning (e.g. `owasp:YYYY:llmXX`) before retagging. Not implementable without a maintainer decision.
- #1499 (paraphrase buff vs transformers): assigned to jmartin-tech.
- Bug issues each with an open PR from other contributors: #2386, #2382, #2381, #2370, #2343, #2336, #2329, #2307, #2299, #2330, #2293, #2291, #2286, #2325, #2323, #2304, #2303.
- #2363 (empty `run.spec` loses precedence to deprecated `probe_spec`): `needs-triage`, zstring commented "happy to take this, will hold for triage". Effectively claimed; low severity.

### Proposal A: garak #2339, make `judge.Jailbreak` fallback visible (warning + docs, optionally use the attempt prompt)

- Problem and users: `garak/detectors/judge.py` line 240 (VERIFIED on main): `goal = attempt.notes.get("attack_goal", attempt.goal) if attempt.notes else attempt.goal`. For probes that do not set `attack_goal` (e.g. `phrasing.PastTense`), the judge sees the probe-level goal sentence as the REQUEST, not the prompt sent to the target, so verdicts are not meaningful while the score looks normal. Anyone pairing `judge.Jailbreak` with non-GOAT probes is affected. Evidence: issue #2339 (filed 2026-10-20 with steps, run on garak 0.16.0, code path unchanged on main).
- Maintainer position (VERIFIED, jmartin-tech 2026-10-20): known limitation introduced with GOAT; using the original prompt as `goal` is viable for only a select number of probes; enhancing probes for a non-primary detector is "not a maintainable pattern"; the intent/technique separation may help. The reporter then asked for a warning or doc note (2026-10-21). The maintainer did not reject that; he did not endorse it either.
- Proposed solution (minimal, in line with the maintainer's stance): when `attack_goal` is absent, emit a once-per-run `logging.warning` naming the detector and probe and saying the judge is evaluating the probe-level goal; add a docstring/reference-docs note on `Jailbreak`. Do NOT change probes. Whether to switch the fallback to `attempt.notes["original_prompt"]` / last prompt message is a design question for the maintainer (the reporter suggested it; the maintainer is skeptical), so propose it as an option only.
- Files: `garak/detectors/judge.py` (class `Jailbreak`, `detect`), `tests/detectors/test_detectors_judge.py` (exists, VERIFIED), docs for the detector.
- Tests and acceptance: unit test that detecting an attempt without `attack_goal` logs the warning exactly once, and an attempt with `attack_goal` logs nothing; existing judge tests still pass; `python -m pytest tests/detectors/test_detectors_judge.py`.
- Effort: about 2-4 hours including reading how `Detector` instances log and are instantiated.
- Risks: warning noise on long runs (mitigate once-per-instance); maintainers may prefer waiting for intent-based path (then PR is closed). There may be an unrelated existing PR touching `judge.py`; I only searched PRs by keyword ("judge Jailbreak goal REQUEST") and found none for this issue (VERIFIED: no PR references #2339), but akhil9tiet asked to be assigned on 2026-10-20 and Kwonhj/jmartin-tech replied without assigning. No PR from akhil9tiet seen as of today.
- Acceptance likelihood: moderate (about 40-55 percent, HYPOTHESIS). Justification: a warning matches what a maintainer already tolerates and what the reporter asked for, it is small and cohesive, and garak merges first-timers regularly; the uncertainty is that the issue is still `needs-triage` and the maintainers could see a warning as noise.
- Maintainer discussion first: YES. AGENTS.md says to comment and await a maintainer reply on `needs-triage` issues. Post one short comment proposing the warning + doc note and asking jmartin-tech whether he wants that or nothing, then wait. Disclose AI assistance in the PR per AGENTS.md.

### Proposal B (secondary): garak #2363, `_map_legacy_selection` treats `run.spec: {}` as absent

- Problem: explicit empty `run.spec` should take precedence over deprecated `plugins.probe_spec` (docstring says "a present `run.spec` wins"); currently `probe_spec: none` wins and silently selects no probes. VERIFIED from issue text (2026-10-27) and zstring's confirmation; I did not run it.
- Fix: presence check (`"spec" in run`) instead of truthiness, plus a regression test. Likely file `garak/_config.py` (function `_map_legacy_selection`; HYPOTHESIS on location, I did not open the file).
- Effort: 1-2 hours. Likelihood: moderate if done, but low value (reporter calls it low severity) and zstring has publicly staged a fix and is waiting for triage. Recommendation: do not pursue unless zstring withdraws; AGENTS.md also discourages one-line busywork PRs.

---

## 4. guardrails-ai/guardrails (mid-sized, low external merge rate)

Purpose: Python framework to validate and structure LLM outputs with validators and re-ask. VERIFIED.

Contribution rules (VERIFIED, `guardrails-CONTRIBUTING.md`): bug fixes and typos may be submitted directly; new features need an issue/Discord first; `make dev`, `make test`, `make autoformat`, `make type`. No AGENTS.md, no PR template, no AI policy found. No `good first issue`/`help wanted` labels in use (0 hits).

Activity (VERIFIED): the 5 PRs merged since 2026-08-06 (#1638, #1625, #1623, #1621, #1616) are all by maintainers CalebCourier / zsimjee. Last external merges I found: #1484 (2026-05-19), #1440 (2026-03-18), #1431 (2026-03-16), each merged by CalebCourier. 45 open PRs, many from external contributors that sit unreviewed (e.g. #1651, #1660, #1661, #1672, #1680, #1684). Recent issues (#1692, #1683, #1657, #1656) have 0 comments. I could not verify a time-to-first-response figure for maintainers; the above is the evidence.

Rejections (all have competing open PRs, VERIFIED by PR search):
- #1657 LiteLLM default model gpt-3.5-turbo: PRs #1660, #1672 open.
- #1683 reask crash for `on="$"`: PR #1684 open.
- #1656 RAIL on_fail default: PRs #1661, #1680 open.
- #1633 sequential vs async fix composition: PR #1651 (equivalence test) open; #1639 closed.
- #1631 telemetry invocation_parameters: PR #1647 open.
- #1559 coerce_to_type "false" is True: PRs #1557, #1627 closed (reason not checked).
- Feature/validator proposals (#1675, #1629, #1488, #1630): promotional or new surface area with no maintainer buy-in.

### Proposal C: guardrails #1692, AsyncValidatorService drops validator-returned metadata

- Problem and users: filed 2026-11-03 with an offline repro (VERIFIED issue body). `SequentialValidatorService` propagates `result.metadata` from a `PassResult` (VERIFIED at lines 181-182, 246-247, 306 of sequential_validator_service.py); `AsyncValidatorService.run_validators` and `async_validate` return the input `metadata` unchanged (VERIFIED by reading `async_validator_service.py`: returns at lines 179, 190, 208; the merge at 254-259 only merges child metadata that is itself the unchanged input). So users of the async path (async guard calls) get different behaviour from sync when a child validator derives metadata that a parent-level validator (`on="$"`) needs.
- Why it matters: sync/async divergence in validation semantics; same family as open #1633, indicating a recurring class of bug.
- Solution: in `AsyncValidatorService.run_validators`, after collecting each validator result, apply the same `if result and result.metadata is not None: metadata = result.metadata` rule used by the sequential service, and ensure `async_validate` returns the updated metadata through the child-to-parent merge (line 254-259, which already has a "TODO address conflicting metadata entries"). Add the issue's repro as a unit test comparing sync vs async metadata.
- Files: `guardrails/validator_service/async_validator_service.py`, tests under `tests/unit_tests/validator_service/` (directory exists, VERIFIED).
- Effort: 3-6 hours (concurrency ordering and conflict semantics are the hard part).
- Risks: async validators run concurrently so "last writer wins" ordering is ambiguous; may collide with fixes for #1633/#1651; behaviour change for users who relied on dropped metadata. I did not run the repro.
- Acceptance likelihood: low-to-moderate (about 25-35 percent, HYPOTHESIS). Justification: clean, tested, offline repro, but external PRs here sit unreviewed and the last external merge I found was 2026-05-19; the maintainers merged only their own work in the last 90 days.
- Maintainer discussion first: yes, recommended. Comment on #1692 with the intended semantics (apply sequential rule, define conflict ordering) and check #1651 so it is not duplicated. Since there is no stated AI policy, still disclose AI assistance as good practice.

---

## Final ranking and recommendation

1. garak #2339 warning + docs (Proposal A): best fit; active responsive maintainer, specific scope, no competing PR, small.
2. guardrails #1692 (Proposal C): real bug with offline repro and no PR, but weak merge throughput.
3. garak #2363 (Proposal B): only if the current claimant withdraws.
4. Inspect AI and promptfoo: no proposals; every accepted/reproduced issue verified so far already has competing PRs. Use review-of-others'-PRs or wait for fresh issues, and apply the AI-disclosure formats exactly.

## Method limits

- Merged-PR counts for promptfoo and Inspect use `gh pr list -L 1000` and hit/neared caps (promptfoo exactly 1000).
- "Claimed" status is judged from comments and PR search by issue number (`in:body,title`); PRs that do not mention the number could be missed. Keyword checks were added only for a few issues.
- I did not clone repos or run any code. Line numbers for garak judge.py (240) and the guardrails services come from the fetched main-branch files saved in evidence (`garak-judge.py`, `guardrails-async_validator_service.py`).
- Time-to-first-response was not computed systematically; anecdotal evidence only, cited inline.
