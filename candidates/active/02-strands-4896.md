# Candidate 2: strands-agents/harness-sdk #4896

| Field | Value |
|---|---|
| Upstream | https://github.com/strands-agents/harness-sdk/issues/4896 |
| Title | Concurrent `MCPClient.load_tools()` calls race during shared-provider initialization |
| Research date | 2026-11-04 |
| Stage | DISCOVER complete. VALIDATE not started. No implementation exists |
| Historical check (2026-11-04) | Open, unassigned, one contributor comment asking a design question, no maintainer reply, no PR, no lock in the code. **Not current. Re-check before acting** |
| Research score | 6.75 (rank 2 of 6) |
| License | Apache-2.0 |

## Problem
One `MCPClient` shared as a tool provider across many concurrently built agents intermittently fails with
`ToolProviderException: Failed to start MCP client: the client session is currently running`.

## Proposed approach (a hypothesis)
Single-flight the start-and-initial-list section of `load_tools()` so one caller initializes and others reuse
the cached result. Open design question: thread lock, asyncio primitive, or per-event-loop guard.

## Maintainer policy
CONTRIBUTING asks contributors to wait for maintainer confirmation before significant work (**ask-first**).
PR template requires a human-written overview and a line-by-line understanding attestation. Maintainers were slow
to reply on `area-mcp` issues (2 of 11 since October); 471 open PRs.

## Technical risks
Deadlock if `start()` re-enters; blocking an event loop with a thread lock; interaction with teardown
(`remove_consumer`); weeks of silence; another contributor has expressed interest.

## Next required decisions (owner)
1. Whether to post an owner-written design comment and wait for a maintainer reply
2. Whether to proceed after a long silence, accepting that the PR may sit unreviewed

## Pointers
Executive report section 2.1 C2 and section 3 recommendation 2; ledger section 1.
