---
name: studio-qa-playtest-lead
description: "Use when you need to coordinate QA plans, playtest scripts, smoke checks, regression tests, bug triage, accessibility checks, and Godot feature acceptance criteria."
---

# Studio QA Playtest Lead

Use for quality gates, bug triage, test plans, smoke checks, regression suites, playtest reports, acceptance criteria, and verification after implementation.

## Load With

- `godot-testing-patterns`
- `godot-debugging-profiling`
- `godot-prompter-godot-testing`
- `gamedev-performance-optimization`
- `studio-ui-ux-game-lead` for accessibility and usability checks.
- `studio-gameplay-lead` for feel/playtest checks.

## QA Gate

Every feature should have:

- Acceptance criteria.
- Smoke path.
- Edge cases.
- Regression risks.
- Manual playtest prompt.
- Evidence to capture: screenshot, log, profiler, save file, export, or replay notes.

## Bug Triage

Classify by:

- Severity: blocker, major, minor, polish.
- Reproducibility.
- Player impact.
- Suspected system.
- Minimal reproduction.
- Next diagnostic action.

## Output

Produce:

- Test matrix.
- Playtest script.
- Bug triage notes.
- Verification evidence required.

## Optional agent playtest

[Autopilot for Godot](https://github.com/ramenvr/autopilot/blob/main/plugin/godot/README.md) documents Godot 4.7+, a separate agent service, Aura sign-in or your own keys, and optional MCP setup for Codex. Follow upstream setup and review its run sharing settings before starting. The project uses Apache-2.0 and includes fonts under SIL OFL. Requirements are from upstream documentation reviewed on 2026-11-09.

Choose exploration to discover issues, testing to exercise an area, verification to check a specific claim, or a goal run to attempt an outcome. Record the build and scene, the claim or goal, steps taken, direct observations, and links to captures or logs. Mark claims confirmed, refuted, or inconclusive. Use inconclusive when the run could not reach the relevant state or evidence is missing. Send ambiguous results and judgments about feel or balance to a human playtester.
