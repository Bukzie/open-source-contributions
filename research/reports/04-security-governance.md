# 04 Security, Auditability and Governance: contribution scouting

Date: 2026-11-04. Research only, read-only gh access. Raw extracts: `research/evidence/security/gh-extracts-2026-11-04.md`.
Labels: VERIFIED = checked via gh with the cited item; HYPOTHESIS = my inference.

## Headline findings

1. VERIFIED: This category is saturated with fast-moving, often AI-looking drive-by PRs. In ossf/scorecard nearly every bug filed in the last three weeks already has an open PR (e.g. #5410, #5399, #5397, #5393, #5390, #5389, #5380 in https://github.com/ossf/scorecard/pulls). In google/osv-scanner several recent PRs were closed unmerged for lacking assignment (#3215, #3203, #3200, #3194, #3191).
2. VERIFIED: Two of four repos have explicit AI-agent rules that gate any Claude-assisted work (zizmor, osv-scanner). Read them before touching anything.
3. VERIFIED: zizmor's policy says the human must read it, not an AI. https://github.com/zizmorcore/.github/blob/main/AI_POLICY.md says "You must not use AI tools to read, understand, or interpret this policy", and zizmor `AGENTS.md` says to stop and show the user the link. I (an AI agent) read it for scouting only; the human owner must read it directly before any contribution, and PRs must use the PR template with AI disclosure.

## Candidate screening

### 1. zizmorcore/zizmor (GitHub Actions static analyzer) - best fit, strictest policy
- Purpose/stack/license: VERIFIED Rust, MIT, 6871 stars, pushed 2026-11-03 (gh api repos/zizmorcore/zizmor).
- Docs: CONTRIBUTING https://github.com/zizmorcore/zizmor/blob/main/CONTRIBUTING.md (VERIFIED: "Good first issues ... leave a comment before opening a PR"); AGENTS.md and CLAUDE.md exist (VERIFIED).
- AI policy (VERIFIED, https://github.com/zizmorcore/.github/blob/main/AI_POLICY.md): AI code welcome with demonstrated human effort; disclosure via PR template; open issue first and wait for maintainer greenlight for non-trivial work; PRs over 750 LOC rejected; behavioral changes need tests; AI-assisted PRs on "good first issue" items are unacceptable (reserved for non-AI newcomers); all communication must be human-written.
- Activity: VERIFIED 146 PRs merged since 2026-08-06 (includes dependabot/bots; most by maintainer woodruffw), latest merge 2026-11-03 (#2521). Responsiveness: VERIFIED #2181 filed 2026-07-12, maintainer replied same day; #2498 filed 2026-10-30, replied same day; #2517 filed 2026-11-02, replied same day. External PRs sit long though: 28 open PRs, oldest 2025-07 (#1010) (VERIFIED list).
- Gaps: new-audit and false-positive issues in abundance (e.g. #2519, #2516, #2496, #2475). Many are claimed in practice by maintainers or regular contributors (#2475 taken by ubiratansoares, 2026-10-22; #2517 maintainer is investigating; #1244 assigned).

### 2. google/osv-scanner (vuln scanner, Go, Apache-2.0) - mid-sized, most competition
- VERIFIED: Go, Apache-2.0, 11387 stars, pushed 2026-11-04, 149 PRs merged since 2026-08-06 (incl. bots; majority by maintainer G-Rath/another-rex). External PRs do merge (#3214 JayOfTheKeyboard, #3169 walterwhite81, both within days).
- AGENTS.md (VERIFIED): strict "Issue Assignment -> Pull Request"; comment, discuss approach, wait for assignment; do not work on assigned issues; conventional commits; run `./scripts/run_lints.sh` and `make test`; extractor/parser bugs belong in google/osv-scalibr, not here.
- Gaps and why rejected: see rejections. SARIF area (#2981, #3093, #3164, #3182) has multiple would-be assignees each (VERIFIED comments), closed competing PRs (#3183, #3200, #2982).

### 3. ossf/scorecard (Go, Apache-2.0)
- VERIFIED: 5809 stars, pushed 2026-11-03, 67 PRs merged since 2026-08-06. Maintainer justaugustus is extremely active, filing and fixing many items directly (#5402, #5378, #5377, tracker #5408 for v5.7.0).
- CONTRIBUTING (VERIFIED): "Identify an existing issue ... The repo owners will respond promptly". No AI policy and no AGENTS.md found (404 on AGENTS.md). Has OpenSpec baselines under `openspec/` (VERIFIED dir listing), suggesting maintainers use spec-driven, probably AI-assisted workflows (HYPOTHESIS).
- Gaps: plenty, but nearly all have open PRs from 5-6 external accounts (see headline). 32 external PRs open at once (VERIFIED list).

### 4. open-policy-agent/conftest (Rego policy testing, Go) - mid-sized
- VERIFIED: Go, 3295 stars, pushed 2026-11-03, license file present though GitHub API says NOASSERTION (did not read LICENSE text; HYPOTHESIS Apache-2.0), 56 PRs merged since 2026-08-06 (mostly dependabot; humans: jalseth, boranx, sarankumar1325, behappymia).
- CONTRIBUTING https://github.com/open-policy-agent/conftest/blob/master/CONTRIBUTING.md (VERIFIED): small fixes straight to PR, large changes issue first, DCO sign-off, conventional commit prefix, tests, squash; v1 migration: master is v1, backport PRs separate against `releases/0.x`. No AGENTS.md and no PR template (VERIFIED dir listing); two open PRs propose AGENTS.md (#1276, #1320) for issue #1234.
- Responsiveness (VERIFIED): PR #1435 opened 2026-09-29 and approved ~9 hours later by jalseth; #1419 approved in 3 days. But many external PRs have zero reviews (#1466, #1467, #1463, #1454, #1443, #1437 open 2-4 weeks). Single effective maintainer (jalseth) (HYPOTHESIS from the above).
- CI already hardened (VERIFIED: `permissions: {}` and ratchet-pinned SHAs in pr.yaml/release.yaml), so issue #1107 (improve Scorecard score) is mostly moot.

Not pursued: gitleaks (VERIFIED: last human-authored merge in recent list is 2026-06-01, #2138; 524 open; slow), CycloneDX/cyclonedx-python (VERIFIED: single maintainer jkowalleck, issues like #675/#648/#735 already have competing open PRs such as #1120). Trivy, Kyverno, Sigstore, in-toto, Semgrep not screened (time); not evidence either way.

## Proposals (3, honestly thin)

### P1. zizmor #2181: flag `benc-uk/workflow-dispatch` in `superfluous-actions`
- Link: https://github.com/zizmorcore/zizmor/issues/2181 (labels enhancement, good first issue, open).
- Maintainer approval: VERIFIED woodruffw 2026-07-12 "I'd be happy to review a PR for that", and 2026-07-13 confirmed the two touchpoints are sufficient: `crates/zizmor/src/audit/superfluous_actions.rs` (SUPERFLUOUS_ACTIONS table) and `docs/audits.md` (~line 1711).
- Not claimed/addressed: VERIFIED no PR found referencing it (pr search by workflow-dispatch); issue author mara004 asked how to do it but said "I'm not a Rust developer" and no PR appeared in about 4 months. HYPOTHESIS: still open to a taker, but comment first as CONTRIBUTING requires. Open PR #2405 edits the same file (rust-toolchain), so expect a trivial rebase.
- Problem/users: workflows using a third-party action to dispatch workflows when `gh workflow run` suffices expose supply-chain surface. Zizmor users miss the hint.
- Solution: add table entry `("benc-uk/workflow-dispatch", "use `gh workflow run` in a script step", Persona::Regular, Confidence::High)` (persona/confidence for maintainer to confirm), docs entry, and a snapshot test fixture like existing superfluous-actions tests (follow dev docs).
- Tests/acceptance: new snapshot test shows the finding; `cargo test`, clippy, docs build pass.
- Effort: 1-2 hours. Risk: very low; wrong persona choice. Acceptance likelihood: high (HYPOTHESIS, backed by explicit invite).
- CRITICAL constraint: VERIFIED policy forbids AI-assisted PRs on "good first issue" items. This one must be written by the human owner, without AI code generation, and comments in their own words. Do not have Claude implement it. Alternatively skip it and leave it for newcomers.
- Discussion first: just the claiming comment.

### P2. zizmor #2484: `unpinned-tools` UX for `version: ${{ vars.X }}`
- Link: https://github.com/zizmorcore/zizmor/issues/2484 (labelled user-experience, filed 2026-10-25, 0 comments, maintainer-authored with two proposed options: lower to pedantic, or allow-list `vars.FOO` in config).
- Not good first issue, so AI-assisted work is allowed in principle, but policy still requires issue greenlight first and a human-owned understanding of the code.
- Risk: HYPOTHESIS the maintainer may implement it directly (merged dozens of PRs in a week; #2476 context). Needs a comment asking which option he prefers and whether he wants a PR. Effort: medium (config schema + audit + docs + tests, under 750 LOC). Acceptance: medium-low (HYPOTHESIS), purely maintainer-driven design.
- Discussion first: yes, mandatory.

### P3. ossf/scorecard #5412 sub-piece: SLSA tooling deprecation (Signed-Releases / Token-Permissions)
- Link: https://github.com/ossf/scorecard/issues/5412 (maintainer-filed 2026-11-03, targets v5.8.0, enhancement, check/Signed-Releases; maintainer asked reviewers if the approach is good).
- Gaps listed in the issue (VERIFIED): `probes/releasesHaveProvenance/impl.go` only matches `.intoto.jsonl`; Token-Permissions workflow matchers in `checks/raw/permissions.go` ~L496-513 name only the old generator; remediation text in `probes/releasesHaveProvenance/def.yml` points to archived repos.
- Proposal: offer to take a bounded slice (for example the `provenance.intoto.json` filename match plus remediation/doc text), with unit tests.
- Risk: HIGH of duplicate effort. The maintainer appears to move at several PRs a day and may implement the whole issue; the area is also heavily trafficked by external accounts. Acceptance: medium (HYPOTHESIS). Discussion first: yes, ask in-issue which slice is free. No AI policy exists, DCO sign-off required (VERIFIED CONTRIBUTING line 13).
- Effort: 0.5-1 day.

## Rejections

| Item | Reason |
|---|---|
| osv-scanner #2981 SARIF level | PR #2982 closed; maintainer G-Rath doubts premise (GitHub uses security-severity); contested by 3+ commenters |
| osv-scanner #3093 SARIF duplicates | assigned to pmig 2026-11-02; PR #3200 raced and closed |
| osv-scanner #3164, #3182 | soujasK / okarin1511 already requested assignment (VERIFIED comments); #3183 closed |
| osv-scanner #3005 | maintainer says not a vuln, code deprecated, may be removed |
| osv-scanner #2875 GitLab format | maintainers deferring until output refactor (comment 2026-06-17) |
| osv-scanner #2145 exit code | maintainer another-rex hesitant on new exit codes (2025-11-13); stale |
| osv-scanner #1938 | stale backlog, no maintainer commitment, speculative |
| osv-scanner #3016 | assigned GitZohair, PR #3178 open; competing #3022 |
| conftest #1396 SARIF ruleId | PR #1425 open, maintainer plans merge post-0.x branch |
| conftest #1234 AGENTS.md | two competing PRs (#1276, #1320) |
| conftest #924 OCI bundle | PR #1443 open; docs fix merged |
| conftest #1203 / #1227 Windows tests | PR #1227 open with 16 reviews |
| conftest #1022 | PR #1437 open |
| conftest #1107 Scorecard score | workflows already pinned, minimal permissions (VERIFIED); maintainer called findings misleading |
| conftest #1462 Go stdlib CVE | release/rebuild task for maintainers |
| scorecard #5314, #5365, #5349/#5348, #5396/#5397, #5379/#5393, #5398/#5399, #5411/#5389 etc. | PRs already open |
| zizmor #2475, #2517, #2498, #2499, #2507 | maintainer or regular contributor engaged; design contested; #2517 maintainer investigating |
| zizmor #1252, #1023, #827, #479, #963 (good first issue) | AI-assisted PRs prohibited on GFI items |
| zizmor #1278 cache-poisoning broadening | HaikalE expressed interest 2026-08-17; noisy FP design; needs design |
| gitleaks, cyclonedx-python | slow/low maintainer throughput or crowded |

## Not verified
- 90-day merged counts include bot PRs; human-only counts were not computed.
- Time-to-first-response was sampled on a handful of items, not computed statistically.
- Trivy, Kyverno, Sigstore, in-toto, Semgrep, Syft/Grype not screened.
- conftest LICENSE text not read.
