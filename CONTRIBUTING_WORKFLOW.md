# Contribution workflow

How a candidate moves from idea to merged or closed. Each project sets its own rules; the upstream
project's actual contribution policy always overrides this document.

```text
DISCOVER -> VALIDATE -> MAINTAINER ALIGNMENT -> OWNER APPROVAL -> IMPLEMENT
  -> INDEPENDENT REVIEW -> OWNER APPROVAL TO SUBMIT -> PR REVIEW -> MERGED / CLOSED
```

| Stage | What happens | Exit condition |
|---|---|---|
| DISCOVER | Find and score an opportunity; record it in `candidates/` | Candidate record exists with upstream link and research date |
| VALIDATE | Fresh checks on the same day: issue state, assignees, competing PRs, upstream AI policy and CONTRIBUTING. Reproduce the problem where applicable | Written evidence of a reproduction and a clean competing-work check |
| MAINTAINER ALIGNMENT | Only where the project asks for it (ask-first, assignment, or design question). Skip where upstream says not to wait | Maintainer reply, or the owner's documented decision to proceed |
| OWNER APPROVAL | Owner approves starting implementation | Entry in `tracking/DECISION_LOG.md` |
| IMPLEMENT | Work in `workspaces/` on a branch of a fork. Focused change, tests, regression coverage | Local tests pass; implementation SHA recorded |
| INDEPENDENT REVIEW | Reviewer who did not materially contribute reviews the exact SHA. QE Gate output, where relevant, is advisory evidence only | Review bound to the SHA; findings resolved or accepted |
| OWNER APPROVAL TO SUBMIT | Owner reads the diff and the PR text, confirms understanding and the AI disclosure | Explicit approval recorded |
| PR REVIEW | Respond to maintainers personally | |
| MERGED / CLOSED | Record the outcome and lessons in `contributions/completed/` | |

## Requirements for every contribution

1. **Fresh checks.** Repeat the issue and competing-PR search on the day work starts and again before submitting.
   Research snapshots go stale in days.
2. **AI policy compliance.** Read the upstream AI policy yourself. Record the rule and how it is met. Some
   projects forbid AI-generated comments or AI-assisted PRs on certain issues; then the owner writes everything.
3. **Reproduction evidence** where the change fixes a defect.
4. **Tests.** Local test run plus focused regression coverage for the change.
5. **Independent review** of the exact implementation SHA.
6. **Human ownership.** The submitter understands every line and can defend it in review.
7. **Owner authorization before every external write**: comments, forks, branches pushed upstream, PRs,
   reactions, issue claims. Approval for one write does not cover the next.

Do not submit AI-generated communication where upstream rules prohibit it. Historical GitHub checks in this
repository are never current verification.
