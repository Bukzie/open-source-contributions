# open-source-contributions

A working record of open-source contribution research, validation and outcomes, kept in the open.

**Status (2026-11-05): research complete, no contribution started.** Nothing in this repository has been
submitted upstream.

## What is here

| Path | Purpose |
|---|---|
| [`research/`](research/README.md) | Scouting reports, the executive synthesis, and a claim-by-claim verification ledger (snapshot of 2026-11-04) |
| [`candidates/`](candidates/README.md) | Six shortlisted opportunities plus backlog and rejected items, with dates, links, risks and policies |
| [`contributions/`](contributions/README.md) | Work in progress and finished contributions (currently empty) |
| [`tracking/`](tracking/CONTRIBUTION_INDEX.md) | Index of every candidate and its stage, and a decision log |
| [`CONTRIBUTING_WORKFLOW.md`](CONTRIBUTING_WORKFLOW.md) | The lifecycle each contribution follows |
| [`docs/`](docs/) | Verification standards, AI-assistance policy, proposed GitHub setup |

## Principles

- Upstream project rules come first, including their AI policies.
- Claims carry dates. A past check is not current verification.
- Every external write (comment, fork, PR) needs explicit owner authorization.
- Submitted work is understood line by line by the person submitting it.

## Candidates at a glance

1. [boxed/mutmut #596](candidates/active/01-mutmut-596.md): Python 3.11 GC crash in stats collection
2. [strands-agents/harness-sdk #4896](candidates/active/02-strands-4896.md): MCP client load_tools race
3. [opentelemetry-python-genai Claude Agent SDK instrumentation](candidates/active/03-otel-genai-claude-agent-sdk.md)
4. [boxed/mutmut #584](candidates/active/04-mutmut-584.md): orphaned process pools
5. [NVIDIA/garak #2339](candidates/active/05-garak-2339.md): silent judge fallback
6. [opentelemetry-python-genai #1022](candidates/active/06-otel-genai-1022.md): Agno batch embeddings

## Notes on the research

Raw evidence (about 200 files of `gh` output and agent working files) is intentionally not published. The
original wildcard-track report was never written; see
[`research/reports/05-wildcard-RECONSTRUCTED.md`](research/reports/05-wildcard-RECONSTRUCTED.md) for what that
file is and is not.
