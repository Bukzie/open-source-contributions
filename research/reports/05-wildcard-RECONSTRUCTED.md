# Wildcard track: reconstructed summary (NOT an original agent report)

> **Provenance warning.** The original researcher report `05-wildcard.md` was never written. The wildcard
> research agent produced raw evidence only (about 45 files under the local-only `evidence/wildcard/`
> archive), and no narrative report, reasoning, or token count survives. This file was written on
> 2026-11-05 during repository preparation. It is a reconstruction from two published sources and from
> reading the raw archive's file list and its `counts.txt` and `candidates.txt`. It is **not** the missing
> agent's work and must not be cited as such.
>
> Sources: [`../summaries/VERIFICATION_LEDGER.md`](../summaries/VERIFICATION_LEDGER.md) section 0 and
> section 5, and [`../summaries/EXECUTIVE_REPORT.md`](../summaries/EXECUTIVE_REPORT.md) sections 1.1, 1.3
> and 6.2. Every statement below is a restatement of those documents. Nothing here was re-checked against
> GitHub on the date of writing. All status claims are as of 2026-11-04.

## What the wildcard track covered

Repositories with raw evidence in the archive: PrefectHQ/fastmcp, simonw/llm,
open-telemetry/opentelemetry-python-genai, Arize-ai/openinference, modelcontextprotocol/inspector,
modelcontextprotocol/python-sdk, open-telemetry/opentelemetry-python-contrib, traceloop/openllmetry.

A label-count screen (`candidates.txt`) listed 11 further repositories: traceloop/openllmetry,
Arize-ai/openinference, ollama/ollama, microsoft/markitdown, open-telemetry/opentelemetry-js-contrib,
Textualize/textual, punkpeye/mcp-proxy, modelcontextprotocol/servers, modelcontextprotocol/registry,
modelcontextprotocol/conformance, modelcontextprotocol/ext-apps.

Discrepancy noted: the executive report says the screen covered "9 more" repositories, and the verification
ledger says 11. The archived `candidates.txt` lists 11 rows, two of which (openllmetry, openinference) are
also profiled above, which may explain the difference. Treat the count as unresolved.

## Outcomes (as of 2026-11-04, from the synthesis stage)

| Item | Outcome | Reason |
|---|---|---|
| opentelemetry-python-genai: claude-agent-sdk instrumentation skeleton | Survivor (candidate 3) | Published package that patches nothing; maintainers stated a design direction; July claim in tracker #141 had no linked PR (status unknown) |
| opentelemetry-python-genai #1022 (Agno batch embeddings) | Survivor (candidate 6) | Maintainer-specified follow-up to PR #738; no PR at the time |
| simonw/llm #1773 | Rejected | Project owner closed the implementing PR on 2026-11-03 and declined the change |
| simonw/llm #1422 | Rejected as a core candidate | Fix belongs to the llm-gguf plugin |
| openinference #4133, #3774 | Rejected | Partly fixed or contested; project requires explicit maintainer confirmation before PRs |
| opentelemetry-python-genai #1035, #1034 | Rejected | Trackers for the reporter's own PR #1033 |
| opentelemetry-python-genai #491 | Rejected | Maintainer-owned design |
| PrefectHQ/fastmcp | No specific candidate | No `prs welcome` issues; only a self-found-bug path exists |

## Known gaps

- The wildcard agent's own reasoning for choosing fastmcp, llm and otel-genai is unknown.
- The token and cost figure for that run is unknown.
- Candidates the agent may have considered but dropped before writing evidence cannot be recovered.
