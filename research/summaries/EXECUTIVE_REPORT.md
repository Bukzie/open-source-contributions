# Open-source contribution scouting: executive report

Date: 2026-11-04. Synthesis stage (Fable). Research and recommendation only. No GitHub writes were made at any stage.

Inputs: `research/BRIEF.md`, four researcher reports (`reports/01` to `04`), raw evidence for all five research tracks under `research/evidence/`, and a fresh read-only re-verification by this stage recorded in `research/evidence/synthesis/` (ledger: `VERIFICATION_LEDGER.md`). Researcher content was treated as evidence to be checked, not as authority.

Owner context used for scoring: builds AI-agent, verification, QA and governance tooling in TypeScript and Python with Claude Code and MCP. Contributions will be AI-assisted, so each project's AI policy is a hard gate, and every issue or PR comment must be written by the owner personally.

---

## 1. Research coverage and key discoveries

### 1.1 Coverage

About 40 repositories were touched across five tracks; 19 were profiled in depth (policy files, 90-day merge counts, open-issue and open-PR cross-referencing). Counts per track:

| Track | Repos profiled | Outcome |
|---|---|---|
| AI agents and orchestration | openai-agents-python, pydantic-ai, smolagents, strands-agents/harness-sdk, crewAI, google/adk-python, modelcontextprotocol/python-sdk, mcp-agent | 1 survivor (Strands #4896); ADK #7867 dropped after re-check |
| Testing, QA, CI tooling | boxed/mutmut, stryker-js, Hypothesis, nektos/act | 2 survivors (mutmut #596, #584); stryker and act dropped |
| AI verification and evaluation | inspect_ai, promptfoo, NVIDIA/garak, guardrails-ai (plus deepeval, lm-evaluation-harness, ragas glanced) | 1 survivor (garak #2339); guardrails dropped |
| Security and governance | zizmor, osv-scanner, ossf/scorecard, conftest (plus gitleaks, cyclonedx-python) | 2 weak survivors (zizmor #2181 human-only, zizmor #2484); scorecard #5412 dropped |
| Wildcard (report never written; reconstructed from evidence) | PrefectHQ/fastmcp, simonw/llm, opentelemetry-python-genai, Arize-ai/openinference, MCP inspector, otel-python-contrib, openllmetry, plus a label-count screen of 9 more | 2 survivors, both in opentelemetry-python-genai (#1022 and the claude-agent-sdk skeleton); llm and openinference candidates refuted |

### 1.2 Categories rejected, and why

- Large agent frameworks (openai-agents-python, pydantic-ai, smolagents, MCP python-sdk, crewAI good-first-issues): either outside PRs are not accepted, maintainers require pre-assignment, or every approachable issue already carries 2 to 12 competing PRs (crewAI #6072 alone has 8 open PRs and a stale bot). Report 01, verified in part.
- Very large or unresponsive repos (nektos/act, stryker-js, Hypothesis design issues, inspect_ai and promptfoo fresh bugs): either zero maintainer presence on community PRs (stryker-js: 0 maintainer reviews or comments on 30 open PRs updated since 2026-10-01; last 10 merges all Renovate) or a race measured in hours against several AI-driven accounts.
- Guardrails-ai: no merges of any kind since 2026-08-26; external PRs sit unreviewed. The #1692 bug is real and unclaimed but there is no evidence it would be reviewed.
- Security scanners with strict assignment gates and heavy traffic (osv-scanner, scorecard): every recent bug has an open PR or an assignee; scorecard's maintainer merged 7 PRs of their own in two weeks, so the one open maintainer-filed issue (#5412) may be handled by the maintainer directly.
- Items refuted on re-check: simonw/llm #1773 (project owner declined the change on 2026-11-03), google/adk-python #7867 (now assigned to a collaborator), openinference #4133 and #3774 (partially fixed or contested, and the project requires explicit maintainer confirmation before any PR), otel-genai #1035 and #1034 (trackers for the reporter's own PR).

### 1.3 Key discoveries

1. Saturation is real and measurable. Across all tracks, well-reproduced bugs in popular repos attract competing PRs within hours or days, many from AI-driven accounts. The only reliable openings are: crash or concurrency bugs in mid-size projects whose issue threads are quiet but whose PR queues still move (mutmut), issues where a maintainer has stated a design opinion that nobody has implemented (garak #2339, otel-genai #1022), and strategic gaps that are too large for drive-by contributors (the otel-genai claude-agent-sdk skeleton).
2. The `opentelemetry-instrumentation-genai-claude-agent-sdk` package on PyPI is an officially listed "skeleton": its `_instrument()` ends with "Patching will be added in a follow-up PR", its tests only check instantiation, the one attempt (PR #297) was closed the day it opened, and the July claim in the migration tracker (#141) has produced no PR in 101 days. The Claude Agent SDK does not emit GenAI spans itself (its `otel` extra only propagates W3C trace context to the CLI subprocess), so the repo's "native instrumentation" policy does not block the work. Maintainers already stated a design direction on 2026-07-18: derive agent and tool spans from the message stream, no hooks. This is the single most strategically relevant opening found, and the hardest.
3. AI policies vary widely and are decisive. zizmor forbids AI-assisted PRs on good-first-issues and requires the human to read the policy without AI help. otel-genai forbids AI-generated comments on issues and PRs outright and asks for an `Assisted-by:` commit trailer. Strands requires a human-written PR overview and a line-by-line understanding attestation. garak requires an AI-use statement, a non-duplication statement, and test output in the PR. mutmut has no written policy and has merged AI-drafted, human-verified work.
4. mutmut's issue threads are nearly silent (1 collaborator comment on 12 issues updated in the last three weeks) but PRs keep merging (6 merges between 2026-10-15 and 10-28, usually without a formal review). The PR is the conversation there.
5. fastmcp has zero `prs welcome` issues, discourages "please assign me" comments, and gives the reporter first claim. The only viable fastmcp path is to find and report a fresh bug and submit the linked fix immediately. External authors do get merged there at high volume, so it remains a good target for a self-found bug, but no specific issue can be shortlisted today.

---

## 2. Ranked shortlist with score table

Weights: usefulness 25, acceptance likelihood 20, feasibility and effort 20, technical learning 15, strategic relevance 15, repository health 5. Sub-scores are 1 to 10. Score = (25U + 20A + 20F + 15L + 15S + 5H) / 100.

| Rank | Candidate | U | A | F | L | S | H | Arithmetic | Score |
|---|---|---|---|---|---|---|---|---|---|
| 1 | boxed/mutmut #596: Python 3.11 GC crash in stats collection | 7 | 7 | 8 | 6 | 6 | 6 | 175+140+160+90+90+30 = 685 | 6.85 |
| 2 | strands-agents/harness-sdk #4896: single-flight `MCPClient.load_tools()` | 7 | 4 | 7 | 8 | 9 | 5 | 175+80+140+120+135+25 = 675 | 6.75 |
| 3 | opentelemetry-python-genai: implement the claude-agent-sdk instrumentation skeleton | 8 | 4 | 3 | 9 | 10 | 8 | 200+80+60+135+150+40 = 665 | 6.65 |
| 4 | boxed/mutmut #584: process-group cleanup for test-spawned pools | 8 | 6 | 6 | 7 | 6 | 6 | 200+120+120+105+90+30 = 665 | 6.65 |
| 5 | NVIDIA/garak #2339: visible fallback in `judge.Jailbreak` (warning, docs, test) | 6 | 5 | 9 | 5 | 8 | 7 | 150+100+180+75+120+35 = 660 | 6.60 |
| 6 | opentelemetry-python-genai #1022: instrument Agno batch embeddings | 6 | 6 | 6 | 8 | 7 | 8 | 150+120+120+120+105+40 = 655 | 6.55 |
| 7 (weak) | zizmorcore/zizmor #2181: flag `benc-uk/workflow-dispatch` as superfluous. HUMAN-ONLY: AI-assisted PRs are prohibited on this issue | 5 | 9 | 5 | 4 | 5 | 9 | 125+180+100+60+75+45 = 585 | 5.85 |
| 8 (weak) | zizmorcore/zizmor #2484: `unpinned-tools` UX for `${{ vars.X }}` versions | 6 | 4 | 6 | 6 | 6 | 9 | 150+80+120+90+90+45 = 575 | 5.75 |

Ranks 3 and 4 tie at 6.65. The tie is broken toward the claude-agent-sdk work because of its strategic value and because rank 1 already sits in mutmut (diversification). Ranks 7 and 8 are marked weak: #2181 cannot be done with AI assistance at all, and #2484 is a maintainer-designed item the maintainer may implement it directly. Only six candidates survive cleanly; the shortlist is not padded beyond that, and candidates that did not survive are listed in section 6.

Feasibility note on rank 7: the score of 5 reflects that the owner would have to write the Rust change, docs entry and snapshot test without any AI help, not that the change is hard (it is a table entry plus a docs line plus a fixture).

### 2.1 Per-candidate detail

#### C1. boxed/mutmut #596: stats collection segfaults on Python 3.11 when a trampolined `__del__` runs during GC

- Issue: https://github.com/boxed/mutmut/issues/596 (opened 2026-10-11, 0 comments, no assignee, no PR; verified 2026-11-04).
- Problem and users: since mutmut 3.7.0 the stats-mode trampoline calls `MutmutCallStack.set()`/`reset()` (a `ContextVar`) on every call, including `__del__`. On CPython 3.10 and 3.11 the cyclic GC can run inside `ContextVar.set()` and re-enter it (CPython use-after-free, fixed upstream for newer versions only), giving exit 139, `TypeError: can't concat int to bytes` or "failed to collect stats". Anyone on 3.10 or 3.11 with a `__del__` in their code base cannot run mutmut 3.7+.
- Why it matters: hard crash with no workaround on Python versions the project says it supports.
- Solution: in `MutmutCallStack.set`/`reset`, when `sys.version_info < (3, 12)`, suspend the cyclic GC around the `ContextVar` call and restore the previous state (`gc.isenabled()`, try/finally). Alternative the maintainers may prefer: skip call-stack tracking inside `__del__`.
- Files: `src/mutmut/core.py` (`MutmutCallStack`, lines 6 to 20 on main), `src/mutmut/mutation/trampoline.py` (lines 94 to 102), tests in `tests/mutation/test_trampoline.py`.
- Evidence: issue body with a 3-file repro; code positions re-verified on main (`evidence/synthesis/code-and-author-rechecks.txt`).
- Tests and acceptance: unit test that `set`/`reset` restore GC state in all branches (already disabled, reset raising); version-gated regression (skip on 3.12+) running the issue's repro through stats collection; `uv run pytest` and `uv run pre-commit run --all-files` green; the repro exits 0 on 3.11.
- Effort: 0.5 to 1 day. Needs a local Python 3.11.
- Risks: per-call `gc.disable()`/`enable()` overhead (measure); thread-safety of toggling global GC state; maintainers preferring the "skip `__del__`" approach; a competing PR appearing (19 open PRs show an active crowd).
- Acceptance likelihood: about 65 percent. For: crash bug with repro and fix, maintainers merge external fix PRs without ceremony (6 merges in two weeks of October). Against: issue thread is silent, so the approach cannot be pre-agreed.
- Discussion first: a short human-written comment is good practice but should not block the PR beyond a day or two; the repo has no ask-first rule and issue replies are rare.
- Learning and strategic value: CPython GC and `ContextVar` internals; mutation testing is adjacent to the owner's QA tooling.

#### C2. strands-agents/harness-sdk #4896: concurrent `MCPClient.load_tools()` calls race during shared-provider initialization

- Issue: https://github.com/strands-agents/harness-sdk/issues/4896 (opened 2026-10-05, labels bug, python, area-async, area-mcp; no assignee; one CONTRIBUTOR comment asking a design question; no maintainer reply; no PR; verified 2026-11-04).
- Problem and users: one `MCPClient` shared as a `ToolProvider` by many agents built concurrently (the reporter runs 50 Langfuse eval items in parallel) intermittently fails with `ToolProviderException: Failed to start MCP client: the client session is currently running`. Hits anyone running concurrent evals or multi-threaded servers against an API-key MCP server.
- Why it matters: concurrency bug in the MCP tool-loading path of a 9k-star SDK; it breaks exactly the evaluation-harness pattern the owner builds.
- Solution: single-flight the start-and-initial-list section of `load_tools()` so one caller initializes and the others wait and receive the cached `_loaded_tools`; keep the sticky `_connection_failed` and teardown semantics unchanged. Open design question (asked by jstar0, unanswered): is cross-thread sharing supported, and should the guard be a `threading.Lock`, an `asyncio` primitive, or per-event-loop?
- Files: `strands-py/src/strands/tools/mcp/mcp_client.py` (`load_tools` at line 526, `start` at 442, flags at 411 to 412, teardown at 624 to 632 on main); tests in `strands-py/tests/strands/tools/mcp/test_mcp_client_tool_provider.py`.
- Evidence: check-then-act without a lock re-verified on main; no `Lock(` in the file; no competing PR by number or keyword; jstar0 has no related PR.
- Tests and acceptance: deterministic regression with N threads gated by a barrier each calling `load_tools()` on a mocked transport; exactly one `start()`, all callers get the same list, no exception; existing tests, `ruff`, `mypy` pass.
- Effort: 1 to 2 days (small diff, careful concurrency test).
- Risks: deadlock if `start()` re-enters; blocking an event loop with a thread lock; interaction with `remove_consumer` teardown; maintainers may be silent for weeks (2 of 11 area-mcp issues since October got a reply; external PRs #4967 and #4848 had no review after 2 to 4 weeks).
- Acceptance likelihood: about 40 percent. For: labelled bug with clear repro, no competing PR, maintainers accepted a similar MCP feature within 3 days on #5236. Against: no maintainer engagement in a month, 471 open PRs, AI-policy attestation requirements.
- Discussion first: yes, mandatory per CONTRIBUTING ("wait for maintainer confirmation before beginning significant work"). The owner posts a short human-written design proposal and waits; code only after a reply, or after a long silence with the risk accepted.
- Learning and strategic value: highest strategic fit of the specific-issue candidates (MCP client lifecycle, agent SDK, eval concurrency).

#### C3. opentelemetry-python-genai: implement `opentelemetry-instrumentation-genai-claude-agent-sdk`

- Tracker: https://github.com/open-telemetry/opentelemetry-python-genai/issues/141 (row "openinference-instrumentation-claude-agent-sdk", assigned to @gh-raju since 2026-07-26, PR #297 closed 2026-07-21). Package: https://github.com/open-telemetry/opentelemetry-python-genai/tree/main/instrumentation/opentelemetry-instrumentation-genai-claude-agent-sdk (README status: skeleton).
- Problem and users: the package is published to PyPI and documented as working, but `_instrument()` creates a `TelemetryHandler` and patches nothing. Users of the Claude Agent SDK on OpenTelemetry get no spans, metrics or events from it.
- Why it matters: a visible gap in the official OTel GenAI instrumentation set for the owner's primary platform; completing it puts the owner in the OTel GenAI SIG's contributor list on the Claude path.
- Solution (as maintainers described on 2026-07-18): observe the SDK's message stream (`query()` and `ClaudeSDKClient`), derive `invoke_agent` and `execute_tool` operations and usage from `AssistantMessage`, tool-use blocks and `ResultMessage`, emit GenAI semantic-convention spans and metrics through `opentelemetry-util-genai`, and do not inject SDK hooks (the Claude Code CLI's native telemetry covers hooks). Split into small PRs: (1) agent span and usage, (2) tool spans, (3) content capture and events, (4) conformance scenarios.
- Files: `instrumentation/opentelemetry-instrumentation-genai-claude-agent-sdk/src/opentelemetry/instrumentation/genai/claude_agent_sdk/{__init__,patch}.py`, `tests/`, `.changelog/`, `tox.ini` entries; OpenInference's `python/instrumentation/openinference-instrumentation-claude-agent-sdk` as the donated reference.
- Evidence: `evidence/synthesis/otel-genai-claude-agent-sdk.txt`, `claude-agent-sdk-claim-liveness.txt`, `claude-agent-sdk-native-tracing.txt`.
- Tests and acceptance: unit tests with a fake transport or recorded SDK messages (no API key), `-oldest` and `-latest` tox envs green, `tox -e typecheck` and `precommit` green, a conformance scenario if the mock server supports it, README updated from skeleton.
- Effort: 1 to 3 weeks across several PRs.
- Risks: the existing tracker claim (2026-07-26) has no linked PR and its status is unknown; maintainers may want the migration-skill "augment mode" followed precisely; semconv for agents is still moving (invoke_agent metrics work in flight); maintainers reply to few issues (3 of 17 external-author issues since mid-October), so alignment may take time; AGENTS.md forbids AI-generated comments, so every discussion message is the owner's own writing.
- Acceptance likelihood: about 35 percent for the whole package, higher for the first small PR once a maintainer re-assigns the row. For: maintainers want it (they created the package and the tracker), stated the design, and merge many external authors (407 merges in 90 days). Against: size, moving conventions, stale claim.
- Discussion first: yes, mandatory. The owner asks in #141 (human-written) whether the claude-agent-sdk row is still taken and whether the message-stream design from 2026-07-18 still holds, and proposes the PR split.
- Learning and strategic value: highest of all candidates (OTel GenAI semconv, util-genai invocation API, Claude Agent SDK internals, conformance tooling).

#### C4. boxed/mutmut #584: process pools started by tests outlive every mutant

- Issue: https://github.com/boxed/mutmut/issues/584 (opened 2026-09-24, 0 comments, no PR; verified 2026-11-04). Reporter offered a PR six weeks ago and has not opened one.
- Problem and users: forked mutant runs end with `os._exit()` and share mutmut's process group, so joblib/loky, `multiprocessing.Pool` and `ProcessPoolExecutor` children survive each mutant. Reporter saw 8,359 orphans and 120 GB RAM exhausted on a 15,800-mutant run; Linux and macOS.
- Why it matters: resource exhaustion that silently kills large mutation runs on any code base that uses process pools in tests.
- Solution: `os.setpgid(0, 0)` in the child right after each fork; after reaping, `os.killpg(pid, SIGTERM)` with optional SIGKILL after a grace period, ignoring `ProcessLookupError`; on timeout signal the group instead of the PID.
- Files: `src/mutmut/workers/isolation.py` (fork sites at lines 85, 142, 396, 577, 853; `os._exit` at 595, 871 on main; no `setpgid`/`killpg` present), `src/mutmut/workers/timeout.py` (line 53), tests in `tests/workers/`.
- Tests and acceptance: a POSIX-only test that a mutant whose test spawns a child leaves zero survivors; timeout verdicts unchanged; E2E snapshots unchanged; Windows path untouched.
- Effort: 1 to 2 days.
- Risks: race between `setpgid` and `killpg`; interplay with the process-isolation feature merged in September; terminal-controlling process group nuance; reporter may still submit.
- Acceptance likelihood: about 50 percent (real impact, clear design, but touches core isolation code and has no maintainer opinion).
- Discussion first: a short human-written comment asking the reporter whether they are still working on it; proceed after a few days of silence.
- Learning and strategic value: process groups, fork and signal semantics; same QA-tooling adjacency as C1.

#### C5. NVIDIA/garak #2339: make the `judge.Jailbreak` fallback visible

- Issue: https://github.com/NVIDIA/garak/issues/2339 (opened 2026-10-20, labels bug and needs-triage, no assignee, no PR; maintainer jmartin-tech replied the same day; reporter asked for a warning or doc note on 10-21; a third party asked to be assigned on 10-20 and has no PR; verified 2026-11-04).
- Problem and users: `garak/detectors/judge.py` line 240 falls back to the probe-level goal as the REQUEST when `attack_goal` is absent, so for probes such as `phrasing.PastTense` the judge never sees the actual prompt and scores look normal. Anyone pairing `judge.Jailbreak` with non-GOAT probes is affected.
- Why it matters: silent evaluation error in a red-teaming tool; the owner's domain is exactly "is this verdict trustworthy".
- Solution: once-per-run `logging.warning` naming the detector and probe when the fallback is taken; docstring and reference-docs note on `Jailbreak`; no probe changes; optionally propose using the original prompt as an opt-in.
- Files: `garak/detectors/judge.py` (class `Jailbreak`, `detect` at line 228), `tests/detectors/test_detectors_judge.py`, detector docs.
- Tests and acceptance: warning logged exactly once for an attempt without `attack_goal`, never with it; existing judge tests pass; `python -m pytest tests/detectors/test_detectors_judge.py`.
- Effort: 2 to 4 hours.
- Risks: maintainers may see a warning as noise or prefer to wait for the intent-based path; AGENTS.md says to wait for a maintainer reply on `needs-triage` issues (5 of 20 recent issues got one).
- Acceptance likelihood: about 45 percent.
- Discussion first: yes. One short human-written comment proposing the warning plus docs and asking jmartin-tech whether he wants it. PR must state AI assistance, non-duplication, and test output, with an attribution trailer and no issue number in the title.
- Learning and strategic value: modest technical learning; strong strategic fit (LLM-as-judge reliability).

#### C6. opentelemetry-python-genai #1022: instrument Agno batch embeddings

- Issue: https://github.com/open-telemetry/opentelemetry-python-genai/issues/1022 (opened 2026-10-31 by maintainer lmolkova, drafted with AI assistance, 0 comments, no assignee, no PR; follow-up to PR #738 which was approved 2026-10-31 and is "waiting on the author" as of 2026-11-04; verified).
- Problem and users: `async_get_embeddings_batch_and_usage` is not instrumented, so batched knowledge inserts through Agno vector stores emit no embedding spans.
- Why it matters: maintainer-specified gap with the quirks already written down (per-chunk requests, repeated usage dicts, per-text fallback already instrumented).
- Solution: patch the batch method in `patch.py` following #738's pattern, one span per provider request or one per call with summed usage (ask which), guard against double instrumentation on the fallback path.
- Files: `instrumentation/opentelemetry-instrumentation-genai-agno/src/opentelemetry/instrumentation/genai/agno/{patch,utils}.py`, `tests/test_embedder.py`, conformance scenario, `.changelog/<PR>.added`.
- Tests and acceptance: `-oldest` and `-latest` tox envs green, typecheck and precommit green, conformance scenario if applicable.
- Effort: 1 to 2 days once #738 merges.
- Risks: approver DylanRussell (author of #738) may do the follow-up directly; must wait for #738; AGENTS.md forbids AI-generated comments.
- Acceptance likelihood: about 55 percent after maintainer alignment.
- Discussion first: yes (human-written comment on #1022 proposing the span shape, after #738 merges).
- Learning and strategic value: the best on-ramp into otel-genai before attempting C3.

#### C7 (weak, human-only). zizmorcore/zizmor #2181: flag `benc-uk/workflow-dispatch` in `superfluous-actions`

- Issue: https://github.com/zizmorcore/zizmor/issues/2181 (good first issue; maintainer woodruffw: "I'd be happy to review a PR for that" on 2026-07-12 and confirmed the two touchpoints on 07-13; no PR; the action is still absent from `crates/zizmor/src/audit/superfluous_actions.rs` and `docs/audits.md`; verified 2026-11-04).
- Hard gate: the zizmor AI policy prohibits AI-assisted PRs on good-first-issue items and requires all communications to be human-authored; the policy itself must be read by the human without AI tools. Claude must not write this code or any comment. Included only because it is the single highest-acceptance item found; the owner decides whether to do it unaided.
- Solution, files, tests: one table entry (`Persona::Regular`, `Confidence::High`, remediation "use `gh workflow run`"), one docs entry, one snapshot fixture; `cargo test`, clippy and docs build.
- Effort: 1 to 2 hours for a human comfortable with Rust tooling.
- Acceptance likelihood: about 85 percent given the explicit invite.
- Discussion first: a human-written claiming comment, as CONTRIBUTING requires.

#### C8 (weak). zizmorcore/zizmor #2484: `unpinned-tools` UX for `version: ${{ vars.X }}`

- Issue: https://github.com/zizmorcore/zizmor/issues/2484 (maintainer-authored 2026-10-25, 0 comments, no PR; two options proposed: lower to pedantic, or allow-list `vars.*` via config; verified).
- Not a good-first-issue, so AI assistance is allowed with disclosure, under 750 LOC, with tests and a prior greenlight.
- Risk: woodruffw merged dozens of PRs in a week and may implement this directly.
- Effort: medium (config schema, audit, docs, tests). Acceptance likelihood: about 35 percent. Discussion first: mandatory (human-written question on which option he prefers and whether an external PR is welcome).

---

## 3. Detailed recommendations for the top three

### Recommendation 1: mutmut #596 (start here)

What the project does: mutmut is a mutation-testing tool for Python. It makes small changes ("mutants") to your code and checks whether your test suite notices. Teams use it to find tests that pass without actually testing anything.

What we would contribute: a fix for a hard crash on Python 3.10 and 3.11. mutmut 3.7 started tracking a call stack in a `ContextVar` on every function call, including object destructors. On older CPython versions the garbage collector can interrupt that call and corrupt memory, so mutmut segfaults. The fix pauses the garbage collector for the microsecond around that call on affected Python versions, with a regression test built from the reporter's repro.

Why it matters: users on supported Python versions cannot use mutmut at all if any class in their project has a `__del__`. The reporter pinned their whole project to Python 3.12 to work around it.

What could go wrong: the maintainers might prefer to simply not track calls inside `__del__`, which is a smaller change; the pause may cost measurable throughput on call-heavy suites (measure and report numbers in the PR); the issue thread will probably stay silent, so the PR must carry its own justification; a competing PR could appear, since this repo has drawn 19 open PRs in five weeks.

Plan: re-check the issue and open PRs; write the human comment (section 5); build a 3.11 environment; reproduce; implement and measure; open the PR with disclosure of AI assistance and the benchmark numbers; expect merge without discussion or a short maintainer edit.

### Recommendation 2: Strands #4896 (start the conversation now, code later)

What the project does: Strands is an open-source SDK (Python and TypeScript) for building production AI agents, with first-class MCP tool support. It is used to run agents that call MCP servers for tools.

What we would contribute: a thread-safe, single-flight initialization for a shared MCP client. Today, if fifty agents are built at once and share one `MCPClient`, several of them try to start the same session simultaneously and some fail. The change makes the first caller do the start-up while the others wait and reuse the result, plus a deterministic test that proves the race is gone.

Why it matters: this is exactly the pattern used by evaluation harnesses and multi-tenant servers, and it is the owner's own domain. The fix is small but requires care about threads versus event loops.

What could go wrong: the maintainers have not replied to this issue in a month and often leave external PRs unreviewed for weeks; the design question (thread lock versus per-loop) is open and a wrong choice would be rejected; another contributor has expressed interest; the PR template requires a human-written overview and an attestation that the author understands every line, which is fine but must be honoured.

Plan: post the human-written design comment on #4896 and wait up to two weeks; meanwhile do recommendation 1. If a maintainer replies, implement within two days. If not, decide whether to submit anyway with the risk that it sits.

### Recommendation 3: the otel-genai claude-agent-sdk instrumentation (ambitious, strategic)

What the project does: opentelemetry-python-genai is the official OpenTelemetry home for Python instrumentation of GenAI libraries (OpenAI, Anthropic, LangChain, Bedrock and others). It emits traces, metrics and events in the standard GenAI semantic conventions.

What we would contribute: the actual implementation behind a package that already exists on PyPI but does nothing. Users who `pip install opentelemetry-instrumentation-genai-claude-agent-sdk` get an instrumentor whose `_instrument()` says "Patching will be added in a follow-up PR". We would observe the Claude Agent SDK's message stream and emit agent and tool spans with token usage, following the design the maintainers themselves outlined in July.

Why it matters: it makes Claude Agent SDK applications observable through the industry standard, is directly useful to the owner's own products, and establishes the owner in the OTel GenAI SIG on the Claude path. It is also the only large opening found that is too big for the drive-by crowd.

What could go wrong: the row in the migration tracker is still assigned to someone from July (no PR since); maintainers reply to few issues, so alignment may take weeks; agent semantic conventions are still changing; the repo forbids AI-generated comments, so every message must be the owner's own; a multi-PR effort can stall after the first PR if review attention moves.

Plan: do C6 (#1022) first as an on-ramp to learn the util-genai APIs and the review culture; in parallel, ask in #141 (human-written) whether the claude-agent-sdk row is free and whether the message-stream design still holds; if yes, deliver PR 1 (agent span plus usage) within a week of the go-ahead.

Also recommended, in brief: C4 (mutmut #584) as the natural second mutmut PR once C1 lands, and C5 (garak #2339) as a two-hour contribution to make once the maintainer answers the human comment.

---

## 4. Quick wins versus ambitious contributions

| Horizon | Candidate | Effort | Gate before coding |
|---|---|---|---|
| Quick win (hours) | garak #2339 warning plus docs | 2 to 4 h | Human comment, wait for jmartin-tech |
| Quick win (one day) | mutmut #596 GC crash | 0.5 to 1 d | Human comment, do not block on reply |
| Quick win, human-only | zizmor #2181 | 1 to 2 h | Human claiming comment; no AI anywhere |
| Medium | mutmut #584 process groups | 1 to 2 d | Human comment to the reporter |
| Medium | strands #4896 single-flight | 1 to 2 d | Human design comment, maintainer reply required |
| Medium | otel-genai #1022 Agno batch embeddings | 1 to 2 d | #738 must merge; human comment |
| Ambitious | otel-genai claude-agent-sdk instrumentation | 1 to 3 weeks, several PRs | Human question in #141, maintainer re-assignment |
| Ambitious, uncertain | zizmor #2484 | 2 to 4 d | Maintainer must choose the option and invite a PR |

---

## 5. Recommended first contribution and its exact first human-written step

First contribution: boxed/mutmut #596.

Why first: it is the only candidate that is a crash with a repro, a small diff, no competitor, no assignment gate, no AI prohibition, and a merge channel that demonstrably works without waiting on issue replies. Strands and otel-genai both require a maintainer reply before code, so their human comments should be posted the same day and left to wait while this one is built.

Exact first step (written by the owner, not by Claude):

1. Open https://github.com/boxed/mutmut/issues/596 and https://github.com/boxed/mutmut/pulls and confirm nothing new has appeared since 2026-11-04 (no comment, no assignee, no PR mentioning GC, `ContextVar`, `__del__` or #596).
2. Post one short comment on #596 in the owner's own words that covers: the owner intends to open a PR; the approach is to suspend the cyclic GC around `MutmutCallStack.set`/`reset` on Python versions below 3.12 and restore the previous state; the PR will include a version-gated regression from the issue's repro and a throughput measurement; the alternative (not tracking inside `__del__`) is available if the maintainers prefer it; and that AI tooling will assist with drafting while the owner verifies every line. Keep it to five or six sentences.
3. Do not wait more than two days for a reply. Create the Python 3.11 environment, reproduce the crash with the issue's three files, then start the implementation.

Same-day secondary steps (also human-written): post the design question on Strands #4896 and the question on otel-genai #141 so their waiting clocks start now.

---

## 6. Evidence links and unresolved questions

### 6.1 Evidence

- Verification ledger: `research/evidence/synthesis/VERIFICATION_LEDGER.md`
- Per-issue fresh checks (state, assignees, last comments, PR mentions, timeline cross-references, keyword PR search): `research/evidence/synthesis/<owner>_<repo>_<n>.txt` for mutmut 596 and 584, strands 4896, adk 7867, stryker 6235 and 6005, garak 2339 and 2363, guardrails 1692, zizmor 2181 and 2484, scorecard 5412, llm 1773 and 1422, otel-genai 1035, 1034, 1022 and 491, openinference 4133 and 3774
- Licenses and metadata: `research/evidence/synthesis/licenses-and-metadata.txt`
- Code-level re-checks (mcp_client.py, judge.py, core.py, trampoline.py, isolation.py, async_validator_service.py): `research/evidence/synthesis/code-and-author-rechecks.txt`
- Competing or closed PRs (#6260, #6231, llm #1777, openinference #4137, otel-genai #738 and #492): `research/evidence/synthesis/pr-followups.txt`
- otel-genai landscape, fastmcp policy signals: `research/evidence/synthesis/fastmcp-and-otel-genai-signals.txt`
- claude-agent-sdk skeleton, claim liveness, native tracing: `research/evidence/synthesis/otel-genai-claude-agent-sdk.txt`, `claude-agent-sdk-claim-liveness.txt`, `claude-agent-sdk-native-tracing.txt`
- Repository health samples: `research/evidence/synthesis/repo-health-spot-checks.txt`, `zizmor-strands-mutmut-health.txt`, `final-checks.txt`
- Researcher reports and raw dumps: `research/reports/01-04`, `research/evidence/{ai-agents,testing-ci,ai-eval,security,wildcard}/`

Key issue URLs:
- https://github.com/boxed/mutmut/issues/596
- https://github.com/boxed/mutmut/issues/584
- https://github.com/strands-agents/harness-sdk/issues/4896
- https://github.com/open-telemetry/opentelemetry-python-genai/issues/141
- https://github.com/open-telemetry/opentelemetry-python-genai/issues/1022
- https://github.com/NVIDIA/garak/issues/2339
- https://github.com/zizmorcore/zizmor/issues/2181
- https://github.com/zizmorcore/zizmor/issues/2484

### 6.2 Candidates that did not survive (with reason)

- stryker-js #6235: real bug, but 0 maintainer reviews or comments on 30 open community PRs in the sampled month and an overlapping unreviewed PR (#6231) since September.
- guardrails #1692: real bug with offline repro, but zero merges of any kind since 2026-08-26.
- scorecard #5412: maintainer-filed and maintainer-driven; 7 maintainer-authored merged PRs in two weeks.
- google/adk-python #7867: assigned to a collaborator on 2026-11-03.
- simonw/llm #1773: owner declined the change on 2026-11-03.
- openinference #4133 and #3774: partially fixed or contested; project requires explicit maintainer confirmation first.
- otel-genai #1035, #1034: reporter's own trackers for PR #1033. #491: maintainer-owned design.
- garak #2363: publicly staged by another contributor; low severity.
- fastmcp: no `prs welcome` issues; only the self-found-bug path exists (worth pursuing opportunistically, not shortlistable today).

### 6.3 Unresolved questions

1. mutmut: do the maintainers prefer GC suspension or skipping `__del__` tracking? What is the per-call overhead on a large suite? Nobody from the project has commented on #596.
2. Strands: is sharing one `MCPClient` across threads and event loops a supported pattern? Thread lock or per-loop guard? Will jstar0 submit first?
3. otel-genai claude-agent-sdk: is the July claim in tracker #141 still active? Does the 2026-07-18 message-stream design still hold after the util-genai stream-wrapper changes (#1033, #872)? Which PR split do maintainers want?
4. otel-genai #1022: when does #738 merge, and will its author do the batch follow-up directly?
5. garak #2339: will jmartin-tech accept a warning, or wait for the intent-based path?
6. zizmor #2484: which option does woodruffw prefer, and does he want an external PR?
7. Wildcard track: the report was never written; the researcher's reasoning for fastmcp, llm and otel-genai is unknown, and the token count for that run is unknown.
8. Not screened at all: Trivy, Kyverno, Sigstore, in-toto, Semgrep, Syft/Grype (security track ran out of time).

---

## 7. Estimated time and model costs

All token figures are approximate and were not metered precisely.

Research already spent:
- Five Sonnet researcher runs, about 25 to 35 minutes wall-clock in parallel. Reported token use: roughly 113k, 122k, 117k and 146k for four runs (about 498k), plus an unknown amount for the fifth run and any subagents those runs spawned. A working assumption for the whole research stage is 600k to 700k tokens.
- This synthesis run (Fable): roughly 20 to 30 minutes wall-clock and an estimated 180k to 220k tokens including tool output (about 60 read-only `gh` calls).
- Total so far: on the order of 0.8M to 0.9M tokens and about one hour of wall-clock. Convert to money using the current list prices for Sonnet and Fable input and output tokens; this report does not assume a price.

Estimated effort to execute the recommendations (owner time, AI-assisted drafting included):
- C1 mutmut #596: 4 to 8 hours of owner time; model use roughly 100k to 200k tokens for code, tests and benchmark iteration.
- C2 Strands #4896: 1 to 2 days once a maintainer replies; roughly 150k to 300k tokens.
- C3 claude-agent-sdk instrumentation: 1 to 3 weeks across several PRs; roughly 1M to 2M tokens; highest variance.
- C4 mutmut #584: 1 to 2 days; roughly 150k to 300k tokens.
- C5 garak #2339: 2 to 4 hours; under 100k tokens.
- C6 otel-genai #1022: 1 to 2 days after #738 merges; roughly 150k to 300k tokens.
- C7 zizmor #2181: 1 to 2 hours, zero model tokens by policy.

Recommended sequence and budget: C1 this week (one day), human comments on C2 and C3 posted the same day, C5 and C6 as the maintainer replies arrive, C3 as a multi-week track if the row is released. Expected first merged PR: C1 within 1 to 3 weeks of opening, judging by mutmut's recent merge cadence.
