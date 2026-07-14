---
name: studio-qa-playtest-lead
description: "Coordinate QA plans, playtest scripts, smoke checks, regression tests, bug triage, accessibility checks, and Godot feature acceptance criteria."
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
