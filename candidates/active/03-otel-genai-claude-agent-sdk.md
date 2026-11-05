# Candidate 3: opentelemetry-python-genai Claude Agent SDK instrumentation

| Field | Value |
|---|---|
| Upstream | https://github.com/open-telemetry/opentelemetry-python-genai/issues/141 (tracker) and the `opentelemetry-instrumentation-genai-claude-agent-sdk` package directory in the same repo |
| Title | Implement the instrumentation behind the published skeleton package |
| Research date | 2026-11-04 |
| Stage | DISCOVER complete. VALIDATE not started. No implementation exists |
| Historical check (2026-11-04) | Package is a documented skeleton; tracker row assigned to another user since 2026-07-26 with no PR; earlier attempt PR #297 closed the day it opened. **Not current. Re-check before acting** |
| Research score | 6.65 (rank 3 of 6, tie-break with #4) |
| License | Apache-2.0 |

## Problem
`_instrument()` creates a handler and patches nothing, so Claude Agent SDK applications get no GenAI telemetry
from the official package.

## Proposed approach (maintainer-stated direction, 2026-07-18)
Observe the SDK message stream, derive `invoke_agent` and `execute_tool` operations and usage, emit through
`opentelemetry-util-genai`, no SDK hooks. Proposed split into several small PRs.

## Maintainer policy
AGENTS.md **forbids AI-generated comments** on issues and PRs and asks for an `Assisted-by:` commit trailer.
Alignment in the tracker is mandatory before code.

## Technical risks
Existing tracker claim (2026-07-26) has no linked PR and its status is unknown; agent semantic conventions still moving; slow maintainer replies (3 of 17
external-author issues since mid-October); multi-week effort; every discussion message must be owner-written.

## Next required decisions (owner)
1. Whether to ask in #141 (owner-written) if the claim is still active and the design still holds
2. Whether to do candidate 6 first as an on-ramp

## Pointers
Executive report section 2.1 C3 and section 3 recommendation 3; ledger section 5.
