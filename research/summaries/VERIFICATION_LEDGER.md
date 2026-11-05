# Synthesis verification ledger

Date: 2026-11-04 (checks run 06:46Z to 06:54Z). Method: fresh read-only `gh` calls only. Nothing was commented, reacted, forked, starred, claimed or created on GitHub.

Raw outputs live in this directory. Each file name is `<owner>_<repo>_<issue>.txt` for per-issue checks, plus the topical files named below.

Status key: VERIFIED = re-observed today with the cited evidence file. REFUTED = today's evidence contradicts the researcher's claim. UNVERIFIED = not re-checked by me; treat as researcher opinion only. PARTIAL = true in part, with the correction stated.

## 0. Structural finding about the inputs

- The fifth report (`reports/05-wildcard.md`) does not exist. Only its raw evidence exists under `evidence/wildcard/` (fastmcp, simonw/llm, opentelemetry-python-genai, openinference, MCP inspector and python-sdk, otel contrib, openllmetry, and a label-count screen of 11 further repos in `candidates.txt`). Every wildcard candidate below was reconstructed from that evidence and verified from scratch. The wildcard researcher's own conclusions are unknown.

## 1. Report 01 (AI agents, orchestration)

| Claim | Status | Evidence |
|---|---|---|
| strands-agents/harness-sdk #4896 open, unassigned, no PR, one CONTRIBUTOR (jstar0) comment, no maintainer reply | VERIFIED | `strands-agents_harness-sdk_4896.txt` (OPEN, assignees empty, 1 comment, no PR mentions, no timeline cross-refs; keyword PR search found no related open PR) |
| `load_tools()` does check-then-`start()` with no lock on main | VERIFIED | `code-and-author-rechecks.txt`: `mcp_client.py` lines 412, 442-455, 526-574; grep for `Lock(` returned nothing; last commit touching the file 2026-10-13 (#4660) |
| jstar0 has not opened a competing PR | VERIFIED | `code-and-author-rechecks.txt`: jstar0's PRs are #3994 and #3337, unrelated |
| Strands maintainers reply slowly to issues | VERIFIED | `zizmor-strands-mutmut-health.txt`: of 11 `area-mcp` issues opened since 2026-10-01, 2 got a MEMBER/COLLABORATOR reply |
| google/adk-python #7867 has no assignee and no PR | REFUTED (assignee) / VERIFIED (no PR) | `google_adk-python_7867.txt`: assigned to surajksharma07 (COLLABORATOR) with a 2026-11-03 comment proposing a workaround; still no PR. Team-owned now; rejected |
| Strands Apache-2.0, ADK Apache-2.0 | VERIFIED | `licenses-and-metadata.txt` |
| openai-agents, pydantic-ai, smolagents, MCP python-sdk rejections | UNVERIFIED | Not re-checked; no shortlisted item depends on them |

## 2. Report 02 (testing, CI, developer tooling)

| Claim | Status | Evidence |
|---|---|---|
| boxed/mutmut #596 open, 0 comments, no PR referencing it | VERIFIED | `boxed_mutmut_596.txt` (only cross-refs are the reporter's own pycubrid issues) |
| No uncited open PR fixes #596 or #584 | VERIFIED | `code-and-author-rechecks.txt`: all 19 open PR titles reviewed; none touch GC/ContextVar/process groups; reporters yeongseon and m-groom have no PRs |
| `MutmutCallStack` ContextVar `set`/`reset` in `core.py`; trampoline calls at lines 94-102 | VERIFIED | `code-and-author-rechecks.txt` (core.py lines 1, 6, 9, 16, 20; trampoline.py 94, 98, 102) |
| #584 fork sites at 85, 142, 396, 577, 853 and `os._exit` at 595, 871; no `setpgid`/`killpg` | VERIFIED | `code-and-author-rechecks.txt` |
| mutmut collaborators reply within 1-2 days on most issues | PARTIAL | `zizmor-strands-mutmut-health.txt`: of 12 issues updated since 2026-10-14, 1 has a collaborator comment. PRs still merge (6 merges 2026-10-15 to 10-28, typically with no formal review). Interpretation: issue threads are a weak channel; PRs are the real channel |
| mutmut BSD-3-Clause | VERIFIED | `licenses-and-metadata.txt` |
| stryker-js #6235 has no PR | VERIFIED | `stryker-mutator_stryker-js_6235.txt`; the one cross-ref (#6260) is an unrelated vitest PR closed as duplicate of #6214 (`pr-followups.txt`) |
| stryker-js #6231 overlaps the same file and is unreviewed | VERIFIED | `pr-followups.txt`: open, updated 2026-11-02, files include `ts-config-preprocessor.ts` and its spec, only a Copilot review |
| stryker-js maintainers are absent from community PRs | VERIFIED (stronger than reported) | `repo-health-spot-checks.txt`: 0 MEMBER reviews and 0 MEMBER comments across 30 open PRs updated since 2026-10-01; last 10 merges are all Renovate |
| Hypothesis is MPL-2.0 (researcher hypothesis) | VERIFIED | `repo-health-spot-checks.txt`: root `LICENSE.txt` says Mozilla Public License v2.0 |
| nektos/act rejections | UNVERIFIED | Not re-checked |

## 3. Report 03 (AI verification and evaluation)

| Claim | Status | Evidence |
|---|---|---|
| NVIDIA/garak #2339 open, `needs-triage`, no PR, akhil9tiet asked, maintainer jmartin-tech gave the position quoted, reporter asked for a warning | VERIFIED | `NVIDIA_garak_2339.txt` |
| `judge.py` line 240 fallback on main | VERIFIED | `code-and-author-rechecks.txt` (line 240; file last changed 2026-08-23) |
| akhil9tiet has not opened a PR | VERIFIED | `code-and-author-rechecks.txt` (empty PR list) |
| garak merges first-time external authors within days | VERIFIED | `repo-health-spot-checks.txt`: last 15 merged PRs include about 9 distinct external authors, created-to-merge 1 to 20 days |
| garak triage backlog | VERIFIED | 5 of 20 issues created since 2026-10-15 got a maintainer reply |
| garak #2363 claimed in comments by zstring | VERIFIED | `NVIDIA_garak_2363.txt` |
| guardrails #1692 open, 0 comments, no PR | VERIFIED | `guardrails-ai_guardrails_1692.txt` |
| `async_validator_service.py` returns input metadata unchanged (lines 179, 190, 208; merge at 254-259 with TODO) | VERIFIED | `code-and-author-rechecks.txt` |
| guardrails merges only maintainers since August | VERIFIED (worse than reported) | `code-and-author-rechecks.txt`: last merge 2026-08-26; no merges at all in the last 10 weeks |
| Inspect AI and promptfoo saturation | UNVERIFIED | Not re-checked; no proposals depend on it |
| garak Apache-2.0, guardrails Apache-2.0 | VERIFIED | `licenses-and-metadata.txt` |

## 4. Report 04 (security, auditability, governance)

| Claim | Status | Evidence |
|---|---|---|
| zizmor #2181 open, `good first issue`, maintainer invite (2026-07-12) and touchpoint confirmation (07-13), no PR | VERIFIED | `zizmorcore_zizmor_2181.txt` |
| `benc-uk/workflow-dispatch` still absent from `superfluous_actions.rs` and `docs/audits.md` | VERIFIED | `zizmor-strands-mutmut-health.txt` (grep returned 0 hits in both files) |
| AI policy forbids AI-assisted PRs on good-first-issue items, requires human-authored communications, forbids AI reading of the policy, 750 LOC cap | VERIFIED | `zizmor-strands-mutmut-health.txt` quotes AI_POLICY.md lines 16-17, 28, 71-75 |
| zizmor #2484 open, maintainer-authored, 0 comments, no PR | VERIFIED | `zizmorcore_zizmor_2484.txt`; no merged PR touching `unpinned-tools` since 2026-10-20 |
| zizmor merges external authors | VERIFIED | `repo-health-spot-checks.txt` (kpab, hashcatHitman, jkanywhere merged 10-22 to 10-31) |
| scorecard #5412 open, maintainer-filed, no competing PR | VERIFIED | `ossf_scorecard_5412.txt`; justaugustus merged 7 PRs of their own since 2026-10-20 (`repo-health-spot-checks.txt`), so the issue may be handled by the maintainer directly |
| conftest license is Apache-2.0 (researcher hypothesis) | VERIFIED | `licenses-and-metadata.txt`: LICENSE header "Licensed under the Apache License, Version 2.0" |
| zizmor MIT, scorecard Apache-2.0 | VERIFIED | `licenses-and-metadata.txt` |

## 5. Wildcard evidence (no report)

| Claim or candidate | Status | Evidence |
|---|---|---|
| simonw/llm #1773 (Python chains unbounded) is open with no PR | REFUTED as a candidate | `simonw_llm_1773.txt` and `pr-followups.txt`: PR #1777 implemented it and was closed by owner simonw on 2026-11-03 with "I'm not going to change this" |
| simonw/llm #1422 (`--no-stream` enters pdb) | REFUTED as a core candidate | Fix belongs to the `llm-gguf` plugin (PR simonw/llm-gguf#17 open since 2026-05-29) |
| PrefectHQ/fastmcp has approachable issues | PARTIAL | `fastmcp-and-otel-genai-signals.txt`: policy requires a linked issue plus assignment unless labelled `prs welcome`; comments asking to be assigned are discouraged; the reporter has first claim. Zero open `prs welcome` issues today. External authors do get merged (500 merges since 2026-08-06 at the query cap; asasemahmed 75, BlueX888 11, mikamikasuki 11, HootRock 10, andreivince 9). Only the self-found-bug path is viable |
| otel-genai #1035 and #1034 are open unclaimed util-genai issues | REFUTED | `open-telemetry_opentelemetry-python-genai_1035.txt` and `_1034.txt`: both filed by eternalcuriouslearner as trackers for their own open PR #1033 |
| otel-genai #491 (abandoned streams leak spans) | PARTIAL | Open, maintainer-filed; PR #492 auto-closed stale 2026-10-14; direction appears to be #872 (execution-scoped invocation context). Maintainer-owned design; not a newcomer target |
| otel-genai #1022 (agno batch embeddings) open, maintainer-authored, no PR, follows #738 | VERIFIED | `open-telemetry_opentelemetry-python-genai_1022.txt`; #738 approved by lmolkova 2026-10-31 and "waiting on the author" as of 2026-11-04 (`pr-followups.txt`) |
| otel-genai `opentelemetry-instrumentation-genai-claude-agent-sdk` is a published skeleton | VERIFIED | `otel-genai-claude-agent-sdk.txt`: README status column says `skeleton`; `__init__.py` says "Patching will be added in a follow-up PR"; tests only test instantiation; PR #297 (initial attempt) closed 2026-07-21 the day it opened with no human comment |
| The claude-agent-sdk package is claimed | PARTIAL (claim status unknown) | `claude-agent-sdk-claim-liveness.txt`: tracker #141 row lists @gh-raju (claimed 2026-07-26); gh-raju has zero PRs in the repo; design guidance from eternalcuriouslearner 2026-07-18 (derive spans from the message stream, no hooks) |
| Claude Agent SDK ships native GenAI tracing (which would block the package under repo policy) | REFUTED | `claude-agent-sdk-native-tracing.txt`: the SDK's `otel` extra only propagates W3C trace context to the CLI subprocess (CHANGELOG #821); gh-raju's gate check in #141 found no `gen_ai.*` emission |
| otel-genai maintainers respond on issues | PARTIAL | `final-checks.txt`: 3 of 17 external-author issues since 2026-10-15 got a maintainer reply; PR review is where attention goes (407 merges in 90 days per `counts.txt`, many external authors in `fastmcp-and-otel-genai-signals.txt`) |
| openinference #4133 (vercel, OTel JS 3.x) is open for a PR | REFUTED as a candidate | `Arize-ai_openinference_4133.txt` and `pr-followups.txt`: #4139 merged the dependency part; #4137 (full SDK 3 support) closed the same day with no comment; a CONTRIBUTOR mapped the remaining work; openinference CONTRIBUTING line 40 requires explicit maintainer confirmation before PRs |
| openinference #3774 (claude-agent-sdk JS Query object) | REFUTED as a candidate | PR #3776 by the reporter is open; #4187 by a second claimant was closed |
| simonw/llm, otel-genai, openinference, fastmcp licenses Apache-2.0 | VERIFIED | `licenses-and-metadata.txt` |

## 6. Discrepancies reconciled

1. Hypothesis license: GitHub API says NOASSERTION; root LICENSE.txt is MPL-2.0. Reconciled: MPL-2.0.
2. conftest license: GitHub API says NOASSERTION; LICENSE header is Apache-2.0. Reconciled: Apache-2.0.
3. ADK #7867: report said unassigned; now assigned to a collaborator. Reconciled: team-owned, dropped.
4. mutmut responsiveness: report measured 1-2 day replies on older issues; last three weeks show near-zero issue replies but steady merges. Reconciled: expect no reply on the issue; the PR itself is the conversation.
5. stryker-js: report said "slow community-PR review"; data shows zero maintainer activity on community PRs for the sampled month. Reconciled: dropped from the shortlist.
6. guardrails: report said "5 merges since 2026-08-06, all maintainers"; the last of those was 2026-08-26 and nothing has merged since. Reconciled: dropped from the shortlist.
7. Wildcard: the missing report's likely top candidate (llm #1773) was rejected by the project owner on 2026-11-03. The surviving wildcard value is in opentelemetry-python-genai.
