# Candidate 6: opentelemetry-python-genai #1022

| Field | Value |
|---|---|
| Upstream | https://github.com/open-telemetry/opentelemetry-python-genai/issues/1022 (depends on PR #738) |
| Title | Instrument Agno batch embeddings |
| Research date | 2026-11-04 |
| Stage | DISCOVER complete. VALIDATE not started. No implementation exists |
| Historical check (2026-11-04) | Open, maintainer-authored, 0 comments, no PR; PR #738 approved but waiting on its author. **Not current. Re-check before acting** |
| Research score | 6.55 (rank 6 of 6) |
| License | Apache-2.0 |

## Problem
`async_get_embeddings_batch_and_usage` is not instrumented, so batched knowledge inserts through Agno vector
stores emit no embedding spans.

## Proposed approach (a hypothesis)
Patch the batch method following the pattern in #738; open question whether to emit one span per provider request
or one per call with summed usage; guard against double instrumentation on the fallback path.

## Maintainer policy
Same repo policy as candidate 3: AI-generated comments forbidden, `Assisted-by:` trailer requested.

## Technical risks
Must wait for #738 to merge; the author of #738 may do the follow-up; moving conventions.

## Next required decisions (owner)
1. Whether to wait for #738 and then post an owner-written span-shape proposal
2. Whether this precedes candidate 3

## Pointers
Executive report section 2.1 C6; ledger section 5.
