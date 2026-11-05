# 01 - AI Agents, Orchestration and Multi-Model Systems: contribution screen

Date of research: 2026-11-04. Method: read-only `gh` CLI (issues, PRs, contents API, search). No comments, reactions, forks, stars or claims were made.
Raw evidence: `evidence/` (local archive, not published) (TSV/TXT dumps referenced below).

Labels: VERIFIED = observed via gh on 2026-11-04 (source given). HYPOTHESIS = my inference, not confirmed.

## 0. Headline finding

This whole category is saturated with AI-agent-generated issues and PRs. In every repo screened, nearly every open "approachable" issue already has 2 to 8 competing open PRs. Three of the five repos formally restrict outside PRs. The only realistic wins are (a) issues with no PR yet and a maintainer-validated design, or (b) self-discovered bugs filed and fixed quickly. Only 2 proposals below survive the filters, and both carry caveats. I did not pad the list to 5.

## 1. Repos screened (6 profiled, 4 deeply)

Summary table (all VERIFIED unless marked; source: `gh api repos/...`, `gh search prs`, evidence files).

| Repo | Stars | License | Last push | Merged PRs, 2026-08-06..11-04 | PR policy for outsiders | Verdict |
|---|---|---|---|---|---|---|
| openai/openai-agents-python | 30,488 | MIT | 2026-11-04 | 544 | PRs from non-collaborators NOT accepted | Reject |
| pydantic/pydantic-ai | 21,020 | MIT | 2026-11-04 | at least 1000 (search cap) | Must be pre-assigned by maintainer | Reject (for now) |
| huggingface/smolagents | 30,204 | Apache-2.0 | 2026-11-03 | 7 | Standard | Reject |
| strands-agents/harness-sdk (formerly sdk-python; ~9k stars, mid-size) | 9,040 | Apache-2.0 | 2026-11-03 | 300+ (list capped at 300 merged, all in ~3 weeks; mostly team + bots) | Open; `ready for contribution` label; ask first | Best fit, with caveats |
| crewAIInc/crewAI | 60,470 | MIT | 2026-11-04 | 410 | Linked open issue required for first-timers; `llm-generated` label required | Fast merges but flooded |
| google/adk-python | 22,100 | Apache-2.0 | 2026-11-04 | 55 | CLA; issue required | Weak for outsiders |
| modelcontextprotocol/python-sdk | 24,749 | MIT | 2026-11-03 | not computed | Must be assigned or `help wanted` | Reject (flooded) |
| lastmile-ai/mcp-agent | 8,575 | Apache-2.0 | 2026-01-25 | n/a | n/a | Rejected as stale (no push in 9 months) |

Notes: merged counts via `gh search prs --merged --merged-at 2026-08-06..2026-11-04`. For strands the search API returned an error after the repo rename, so the 300 figure is a capped `gh pr list` and is only a lower bound.

### 1.1 openai/openai-agents-python (REJECT)
- VERIFIED: `CONTRIBUTING.md` states "Pull requests are limited to repository collaborators. We do not accept pull requests from non-collaborators, including documentation or example changes." Issues, repros and root-cause analysis are welcome. https://github.com/openai/openai-agents-python/blob/main/CONTRIBUTING.md (copy in `openai-agents-contrib.txt`).
- VERIFIED: ~35 open issues (list in `openai-agents-open-issues.tsv`), real bugs exist (e.g. #5459 SQLAlchemySession ordering on PostgreSQL, #5474 MCPServerStreamableHttp serializing parallel calls) but a PR cannot be contributed. Only possible contribution is a high-quality issue/repro, which is outside this mission's PR goal.

### 1.2 pydantic/pydantic-ai (REJECT for now)
- VERIFIED policy (`docs/contributing.md`, copy in `pydantic-ai-contrib.txt`): "Make sure a maintainer has agreed to the approach on the issue and assigned you. Then open a PR." "Unassigned PRs may be auto-closed." "PRs on issues we have not pre-aligned on are not in our review queue." They may rewrite or supersede contributed code. For well-scoped bugs "we may generate a fix internally".
- VERIFIED AI policy: `AGENTS.md` tells coding agents to steer users to a clear issue or a `PLAN.md`, and says long AI-generated issues are likely to be ignored.
- VERIFIED: no `good first issue` or `help wanted` label exists (label list in `pydantic-ai-labels.tsv`). Open `bug` issues are mostly authored by maintainers or bots (labels `pydanty:*`, `parked:no-user-report`).
- Not measured: median first-response time (not computed). Reject because the contribution path has no dependable entry point and credit is not guaranteed.

### 1.3 huggingface/smolagents (REJECT)
- VERIFIED: only 7 PRs merged in 90 days (`gh search prs`), yet 40 most recent PRs (`smolagents-recent-prs.tsv`) are 36+ open, many duplicates (e.g. 5 open PRs for the `print(sep/end)` fix: #3092, #3083, #3065 and others; 4 for genexp laziness).
- VERIFIED: of 64 issues opened 2026-10-01..10-19, 0 had a comment from a MEMBER/OWNER/COLLABORATOR (`response-times-issues.txt`).
- Rejected: maintainers are effectively not merging; any PR would join a pile of duplicates.

### 1.4 strands-agents/harness-sdk (BEST FIT, mid-size)
- Purpose/stack: VERIFIED, "Open-source SDK for production AI agents in Python & TypeScript"; monorepo with `strands-py/`, `strands-ts/`, `site/`. Apache-2.0. https://github.com/strands-agents/harness-sdk (the old URL strands-agents/sdk-python redirects here).
- Policy: VERIFIED `CONTRIBUTING.md`: label `ready for contribution` marks issues open to the community; "Check if someone is already assigned", "Comment on the issue", "Wait for maintainer confirmation before beginning significant work". `AGENTS.md` and PR template require a human overview in the author's own words ("An AI agent MUST NOT fill out this section", references `team/AI_USAGE_POLICY.md`) and a checkbox attesting the author understands every line, including AI-generated ones. Copy: `strands-contrib.txt`.
- Activity: VERIFIED. ~1,100 open items; 471 open PRs (`gh pr list --state open`).
- Responsiveness: VERIFIED but noisy. For issues created 2026-10-01..10-19 (121 issues), only 16 got a MEMBER/OWNER/COLLABORATOR comment, median 193 h to that reply (p25 33 h, p75 326 h) (`response-times-issues.txt`). Caveat HYPOTHESIS: the team's bot account `strandly-the-agent` (46 of the last 200 merged PRs) may be counted differently from humans.
- External PRs are slow: VERIFIED example, PRs #4967 and #4848 had zero reviews or comments 2+ and 4+ weeks after opening (`strands-pr-status.txt`). One external PR was merged within a day (#5166 by Katsuhito04, merged by a maintainer 2026-10-17), and community docs/site contributors merge quickly.
- Competition: VERIFIED. Of the 37 `ready for contribution` issues (`strands-labeled-issues.tsv`), nearly all have open competing PRs (cross-reference in `strands-issue-pr-crossref.txt`), e.g. #4461 has 5 open PRs, #5236 has #5477, #4544 has #4967 plus three people who asked to take it.
- Maintainer invitation example: VERIFIED, on #5236 maintainer Unshure (MEMBER) wrote on 2026-10-22 "I would be happy to accept a feature like this, feel free to open a pull request."

### 1.5 crewAIInc/crewAI (flooded, but the fastest merger of outsiders)
- Policy: VERIFIED `.github/CONTRIBUTING.md`: "AI-Generated Contributions ... the `llm-generated` label is required"; unlabeled AI contributions "may be closed without review". PR template: first-time contributors must link an existing open issue or the PR is auto-closed with `needs-issue`. `AGENTS.md`: docs under `docs/edge/en/*`, translations to ar, ko, pt-BR required. Copies: `crewai-contrib.txt`, `crewai-contributing.txt`.
- Activity: VERIFIED 410 merged PRs in 90 days, 634 open PRs.
- Merge speed: VERIFIED in `crewai-merged-prs.tsv`: maintainer Vidit-Ostwal merges outside contributors' fix PRs within 0 to 3 days (e.g. Kiko0301 #8561/#8568/#8570/#8572 merged 2026-10-26; Wilson0511 #8617, #8642; subhashpolisetti #8648). These contributors found and fixed bugs themselves, typically opening the PR within a day of the issue.
- Invited work: VERIFIED. Maintainer lorenzejay (author) labelled ~15 issues `good first issue` / `help wanted` / `llm-generated` / `student-project` (#8002, #8003, #8009 to #8011, #8069, #8005 to #8008). Each is already claimed in comments and has 3 to 8 open PRs (e.g. #8009 Groq routing: #8013, #8027, #8035, #8661, #8801, #8826; #8069: six PRs). VERIFIED: none of these good-first-issue tickets were closed by a merged PR as of today (`crewai-closed-gfi.tsv` shows the 3 recently closed ones were from September).
- Promotional flag: VERIFIED #8065 to #8068 and Strands PR #5590/#5240 reference a vendor ("Jev", decisionapi.net). HYPOTHESIS: vendor integration pitches, avoid.
- 56 open bugs checked (`crewai-open-bugs.tsv`). VERIFIED: all but one (#8063, an empty "[BUG]" with no content) had at least one open PR (`crewai-issue-pr-crossref.txt`).
- First-response: the measured sample (2 of 137 issues with a maintainer-association reply) is too small to trust; not reported as a median.

### 1.6 google/adk-python (weak for outsiders)
- VERIFIED `CONTRIBUTING.md`: CLA required; "All PRs, other than small documentation or typo fixes, should have an Issue associated"; changes land via Copybara as a separate commit (`adk-contributing.txt`).
- VERIFIED responsiveness: 51 of 77 issues opened 10-01..10-19 got a team reply, median 38.7 h (p25 16 h, p75 70 h).
- VERIFIED: the 100 most recent merged PRs are authored by `adk-bot`, GWeale, copybara-service, wuliang229, wukath etc. (`adk-merged-prs.tsv`). I could not verify the rate at which external PRs land via Copybara. The open issue list is dominated by three accounts (surajksharma07, llalitkumarrr, sanketpatil06) whose issues share a distinct style; surajksharma07 is marked COLLABORATOR on #7867, so these are team or team-adjacent. 236 open PRs.

### 1.7 modelcontextprotocol/python-sdk (REJECT)
- VERIFIED `CONTRIBUTING.md`: outside PRs reviewed only if the linked issue is assigned to you or labelled `help wanted`; otherwise a bot closes them. AI use must be disclosed (one line); undisclosed AI contributions may be closed; repeated cases can lead to org block. Copy: `mcp-python-sdk-contributing.txt`.
- VERIFIED: only 1 `help wanted` issue (#1723, `needs decision`, two competing open PRs #3516, #2065) and 6 `good first issue`s. Each of #1933, #1401, #156, #348, #226 has 5 to 8 closed or open competing PRs (`mcp-candidates.txt`, crossref in transcript). #1933 appears already fixed on main (comment 2026-09-28).

## 2. Proposals

### P1. Strands: single-flight startup for shared `MCPClient` tool provider (issue #4896)

- Issue: https://github.com/strands-agents/harness-sdk/issues/4896 (labels bug, python, area-async, area-mcp; opened 2026-10-05). VERIFIED no assignee, no linked or cross-referenced PR (`gh pr list --search 4896` returned nothing, 2026-11-04).
- Problem and users: one `MCPClient` shared as a `ToolProvider` by many agents constructed concurrently (reporter runs 50 parallel Langfuse eval items) intermittently fails with `ToolProviderException: Failed to start MCP client: the client session is currently running`. VERIFIED from issue body. Users with API-key MCP servers in eval harnesses or multi-threaded servers hit it.
- Evidence in code (VERIFIED by reading main `strands-py/src/strands/tools/mcp/mcp_client.py`): `load_tools()` checks `if not self._tool_provider_started:` and then calls `self.start()`; `start()` raises `MCPClientInitializationError("the client session is currently running")` when `_is_session_active()`. There is no lock between the check and `start()`, so two callers racing both enter `start()`. The loaded-tools cache `_loaded_tools` has the same check-then-act shape. HYPOTHESIS: this is the whole root cause (not reproduced locally).
- Proposed solution: add a `threading.Lock` (single-flight) around the start-and-initial-list section so one caller initializes and the others wait and receive the cached `_loaded_tools`. Keep the sticky `_connection_failed` semantics and teardown reset unchanged. The design question raised by contributor jstar0 on the issue (is cross-thread sharing supported; single-flight versus one event loop) needs a maintainer answer first.
- Files: `strands-py/src/strands/tools/mcp/mcp_client.py`; tests in `strands-py/tests/strands/tools/mcp/test_mcp_client_tool_provider.py` (file exists, VERIFIED).
- Tests and acceptance: deterministic regression with N threads each calling `load_tools()` through a gate (barrier) on a mocked transport; assert exactly one `start()`, all callers get the same tool list, no `ToolProviderException`; existing tests, `ruff`, `mypy` per `strands-py/AGENTS.md` pass; continue_on_error and teardown tests unchanged.
- Effort: 1 to 2 days (small diff, careful concurrency test).
- Risks: lock held across blocking `start()` could deadlock if `start()` re-enters; interaction with `remove_consumer` teardown; event-loop affinity for async callers (a `threading.Lock` blocks the loop, consider `asyncio` versus thread locking since `load_tools` is async and called from separate loops).
- Acceptance likelihood: MODERATE (HYPOTHESIS). For: real user-reported bug in an area the maintainers maintain, label `bug` with a clear repro, no competing PR, maintainers say they accept features/fixes with PRs on similar issues (#5236). Against: median maintainer reply on issues is slow (193 h), external PRs often sit unreviewed for weeks, another contributor (jstar0, CONTRIBUTOR, 2026-10-05) expressed interest and could open a PR any day.
- Maintainer discussion first: YES. Post a short plan (single-flight design, lock type) on #4896 and wait for a team reply before coding, per CONTRIBUTING. Re-check for new PRs immediately before starting.
- AI note: Strands requires a human-written overview in the PR and attestation that the author understands every line.

### P2. google/adk-python: case-sensitive keys for `DatabaseSessionService` on MySQL/MariaDB (issue #7867)

- Issue: https://github.com/google/adk-python/issues/7867 (label services; opened 2026-10-30; VERIFIED no cross-referenced PR). Filed by a team-associated account; surajksharma07 (COLLABORATOR) confirmed on 2.13.0 that `schemas/v1.py` creates plain `VARCHAR(128)` key columns without a collation and suggested a workaround.
- Problem and users: on MySQL/MariaDB default collation, user ids `"Alice"` and `"alice"` (and accented variants) are the same key, so one user can read another user's session, events and `user:` state. This is a data isolation issue for multi-user deployments on MySQL/MariaDB. `InMemory`, `Sqlite` and PostgreSQL behave correctly. VERIFIED from the issue.
- Proposed solution: declare a binary or case-sensitive collation on the key columns for MySQL/MariaDB dialects (e.g. `String(..., collation="utf8mb4_bin")` via a dialect-conditional type), plus a documented migration note for existing schemas. Note MariaDB `utf8mb4_bin` is still PAD SPACE, so trailing-space keys collide; document or validate.
- Files: `src/google/adk/sessions/schemas/v1.py` (named in the issue; not read by me), database session service and its tests.
- Tests: MySQL/MariaDB-specific tests are probably hard in CI (HYPOTHESIS); at minimum a unit test that checks the generated DDL for the MySQL dialect and a docs note. Acceptance: DDL for MySQL has case-sensitive collation; SQLite/PostgreSQL DDL unchanged.
- Effort: 2 to 3 days including migration design.
- Risks: schema change for existing deployments (migration/compat), possibly needs the schema versioning (`v1`) strategy; maintainers may want to fix internally.
- Acceptance likelihood: LOW to MODERATE (HYPOTHESIS). For: team confirmed the bug; no PR yet; ADK replies to issues fast (median 38.7 h). Against: I could not verify any external PR landing in the last 100 merges (authors are team and bots), the schema/migration decision is the maintainers' call, and the issue came from the team so they may already plan to fix it.
- Maintainer discussion first: YES. Ask on the issue which collation and migration approach they want, and whether they would accept an external PR, before writing code. Requires signing the Google CLA.

## 3. Rejected items (reason)

| Item | Reason |
|---|---|
| openai-agents-python, all issues | PRs not accepted from non-collaborators (VERIFIED CONTRIBUTING). |
| pydantic-ai, all items | Requires maintainer assignment first, unassigned PRs may be closed, maintainers may rewrite; no help-wanted path; core issues are mostly maintainer-authored. |
| smolagents, all items | 7 merges in 90 days, 0 maintainer replies on 64 recent issues, many duplicate PRs. |
| MCP python-sdk #1933, #1401, #156, #348, #226 | Each has 5 to 8 competing PRs, 4 closed by the bot; #1933 appears fixed on main. |
| MCP python-sdk #1723 | `needs decision`, 2 open PRs. |
| mcp-agent | Stale, last push 2026-01-25. |
| Strands #4838 (http_request timeout) | Already has PR #4848 (open). |
| Strands #4461 (UTF-8 across 64 KiB boundary) | 5 open competing PRs (#4755, #4695, #5067, #4463, #5056). |
| Strands #4544, #4531 (OpenAI client / image detail) | PRs #4967, #4966 open; 3+ people also asked to take #4544. |
| Strands #5236 (MCP meta_provider) | PR #5477 open; maintainer approved the idea but a contributor already submitted. |
| Strands #4425, #3299, #2156, #1819, #1436, #1261, #1247, #1216, #1165, #1066, #1059, #843, #689, #522, #264, #1642, #1720 | Each has at least one open PR (`strands-issue-pr-crossref.txt`), several of them months stale (low review velocity). |
| Strands #5804 (Ollama reasoningContent TypeError, opened today) | Reporter wrote "I noticed things I could fix" (likely to self-PR) and older PR #1051 (open since 2025-10-19) already covers both defects. |
| Strands #2572, #2567, #2582, #2584 (docs) | Docs requests; #2582, #2584 have PRs (#2912, #3586); #2572 is low-value without a specific target. |
| CrewAI #8002, #8003, #8069, #8009 to #8011, #8006, #8008 | Claimed and each has 2 to 8 open PRs (VERIFIED); student-program style tickets. |
| CrewAI #8065 to #8068 | Vendor ("Jev") integration pitches, promotional. |
| CrewAI #6072, #7252, #5802 | #6072 has 7 open PRs; #7252 assigned (bunnysayzz); #5802 is a 100-comment design discussion. |
| CrewAI #8680, #8098, #8434, #7466, #7987, #7970, #8370, #8195, #8219, #8320, #8091, #7473, #7684, #7746, #8316, #8338, and all checkpoint bugs (#8437 to #9022) | All have open competing PRs (`crewai-issue-pr-crossref.txt`). |
| CrewAI #8063 | Empty "[BUG]" issue, not actionable. |
| ADK #7983, #7956, #7914, #7900, #7890, #7838, #7793, #7804, #7740, #7906 | Each already has one or more open PRs. |

## 4. Practical guidance (HYPOTHESIS unless stated)

- CrewAI is the only repo where outsiders demonstrably get merged within days (VERIFIED), but only by finding a fresh bug, filing an issue and opening a tested PR the same day. A reasonable strategy is to read recently merged areas (checkpoint/restore, MCP, files, knowledge) and look for unreported defects rather than pick listed tickets. This requires fresh code investigation which I did not do; no specific CrewAI proposal is therefore offered.
- Before acting on any proposal, re-check the issue for new PRs and comments; the counts above change daily.
- All repos screened require disclosure or labelling of AI-assisted work; follow each rule (Strands human overview, CrewAI `llm-generated`, MCP one-line disclosure).

## 5. Limits of this research

- Maintainer response medians use `authorAssociation` of the first MEMBER/OWNER/COLLABORATOR comment on issues created 2026-10-01..10-19; bot or app comments are not excluded in all cases, and sample sizes are small for CrewAI.
- PR coverage was determined with `gh pr list --search "<number> in:title,body"`, which misses PRs that fix an issue without mentioning its number.
- Pydantic AI median response time and MCP SDK merged-PR count were not computed.
- I did not clone or run any code; code claims come from reading files via the contents API.
- Evidence files not listed above: `pydantic-ai-labels.tsv`, `strands-merged-prs.tsv`, `strands-open-python-bugs.tsv`, `strands-bug-validated.tsv`, `crewai-merged-prs.tsv`, `adk-open-issues.tsv`, `adk-issue-pr-crossref.txt`, `mcp-python-sdk-labeled.tsv`.
