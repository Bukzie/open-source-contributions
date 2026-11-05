# Candidates

A candidate is a specific upstream issue or gap that research found worth validating. A record here is **not** a
commitment and **not** evidence that work has begun. Status words follow the lifecycle in
`../CONTRIBUTING_WORKFLOW.md`.

All six records below were researched on 2026-11-04 and are at the end of DISCOVER. Their "historical check"
lines describe what was observed that day, not the present.

## Active (shortlisted)

| # | Record | Upstream | Score | Stage |
|---|---|---|---|---|
| 1 | [mutmut #596](active/01-mutmut-596.md) | https://github.com/boxed/mutmut/issues/596 | 6.85 | DISCOVER done |
| 2 | [Strands #4896](active/02-strands-4896.md) | https://github.com/strands-agents/harness-sdk/issues/4896 | 6.75 | DISCOVER done |
| 3 | [otel-genai claude-agent-sdk](active/03-otel-genai-claude-agent-sdk.md) | https://github.com/open-telemetry/opentelemetry-python-genai/issues/141 | 6.65 | DISCOVER done |
| 4 | [mutmut #584](active/04-mutmut-584.md) | https://github.com/boxed/mutmut/issues/584 | 6.65 | DISCOVER done |
| 5 | [garak #2339](active/05-garak-2339.md) | https://github.com/NVIDIA/garak/issues/2339 | 6.60 | DISCOVER done |
| 6 | [otel-genai #1022](active/06-otel-genai-1022.md) | https://github.com/open-telemetry/opentelemetry-python-genai/issues/1022 | 6.55 | DISCOVER done |

## Backlog (weak survivors, not shortlisted)

| Item | Upstream | Why held back |
|---|---|---|
| zizmor #2181 | https://github.com/zizmorcore/zizmor/issues/2181 | Highest acceptance signal (maintainer invited a PR), but the project's AI policy prohibits AI-assisted PRs on good-first-issues and requires human-authored communication. Human-only, owner decision |
| zizmor #2484 | https://github.com/zizmorcore/zizmor/issues/2484 | Maintainer-authored design; maintainer authored the design; no external-PR invitation recorded; needs a greenlight first |

## Rejected (with reasons as of 2026-11-04)

| Item | Reason |
|---|---|
| stryker-js #6235 | No maintainer activity on community PRs in the sampled month; overlapping unreviewed PR |
| guardrails-ai #1692 | No merges of any kind since 2026-08-26 |
| ossf/scorecard #5412 | Maintainer-filed; the maintainer was actively merging their own PRs |
| google/adk-python #7867 | Assigned to a collaborator on 2026-11-03 |
| simonw/llm #1773 | Project owner declined the change on 2026-11-03 |
| openinference #4133, #3774 | Partly fixed or contested; explicit maintainer confirmation required first |
| otel-genai #1035, #1034, #491 | Trackers for the reporter's own PR, or maintainer-owned design |
| garak #2363 | Staged by another contributor; low severity |
| fastmcp | No `prs welcome` issues today; only a self-found-bug path remains |
| Large agent frameworks (openai-agents-python, pydantic-ai, smolagents, MCP python-sdk, crewAI) | Outside PRs not accepted, pre-assignment required, or many competing PRs |
| nektos/act, Hypothesis design issues, inspect_ai, promptfoo | Little observed maintainer activity on community PRs, or races against automated accounts |

Some rejections were verified on 2026-11-04 and some were researcher opinion only; the ledger
(`../research/summaries/VERIFICATION_LEDGER.md`) marks which. Not screened at all: Trivy, Kyverno, Sigstore,
in-toto, Semgrep, Syft/Grype.
