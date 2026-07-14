---
name: gamedev-game-jam
description: "Imported awesome-gamedev-agent-skills guidance for game-jam workflows in game development projects."
---
# Game Jam

Turn a theme and a fixed deadline into a finished, submitted game. This is a planning and
scope-control playbook, not engine code: the win condition is *something submitted and
playable*, not *the game you imagined*.

## When to use

- Use when entering a timed jam (Ludum Dare, GMTK Jam, Global Game Jam, a weekend jam),
  scoping a 48-hour build, or deciding what to cut to hit a deadline.
- Use when the user asks "what can I actually build in a weekend" or "how do I submit to
  this jam".

**When *not* to use:** building the *core loop* in engine code (use the engine skill —
`godot-2d-movement`, `phaser-core`, etc. — or a genre skill like `platformer`); throwaway
experiments with no deadline (use `prototype-fast`); shipping a commercial release (use
`steam-publish` / `itch-publish`).

## Core workflow

1. **Read the rules before the theme drops.** Confirm the jam's *length*, *theme reveal
   time*, *submission deadline (with timezone)*, whether teams/pre-made assets/engines are
   allowed, and whether ratings require you to rate other entries. Missing one of these
   disqualifies an otherwise-finished game.
2. **Prep the boring parts in advance** (allowed by most jams): empty project that builds
   and exports, input + a title/end screen stub, an export pipeline you've run once, and a
   font/SFX source you're licensed to use. Day-one time is too precious to spend here.
3. **Theme → one sentence.** Brainstorm 10 ideas in 15 minutes, then commit to **one**
   expressible as: *"You [verb] to [goal] while [constraint]."* If you can't say it in one
   sentence, it's too big.
4. **Scope to the clock, not the idea.** Use the budget table below. Pick **one** core
   mechanic and **one** "hook". Everything else is a stretch goal.
5. **Build the vertical slice first.** Get a 30-second playable loop (start → play → lose/win
   → restart) running early. A complete tiny loop beats a half-built big one.
6. **Reserve the last ~20% of the clock for shipping**, not features. Export, test the build
   on a clean path, capture screenshots, write the page. Builds always break at hour 47.
7. **Submit early, update if time remains.** Upload a working build *well before* the
   deadline; most jam pages let you swap the file until it closes. A submitted mediocre game
   scores; an unsubmitted great one does not.

## Patterns

### 1. Scope budget by jam length (plan backwards from the deadline)

```text
              | 48-hour jam            | 72-hour jam           | 1-week jam
--------------|------------------------|-----------------------|------------------------
Core mechanic | 1, proven by hour 6    | 1-2                   | 2-3 interacting
Levels/content| 1 hand-made or gen'd   | 3-5                   | 8-12 + progression
Art           | placeholder/1 palette  | cohesive 1-artist set | themed set + UI
Audio         | 3-5 SFX + 1 loop       | SFX + 1-2 tracks      | adaptive music
SHIP BUFFER   | last 8-10 h            | last 12-16 h          | last full day
```

### 2. The 48-hour timeline (concrete blocks)

```text
H0-2    Ideate -> lock ONE-sentence concept -> name the core mechanic + win/lose.
H2-8    Core loop in code with primitives (boxes/circles). Make it playable, no art.
H8-12   Sleep. (Tired code is tomorrow's bug list.)
H12-24  Content: 1 level/encounter, tune difficulty, add the "hook" feature.
H24-30  Sleep + playtest with one other person; cut anything not landing.
H30-38  Art + audio pass. Juice: screenshake, hit-stop, tween, particles, SFX.
H38-44  Bug-fix freeze: no new features. Fix only crashes + soft-locks.
H44-48  EXPORT, test the build clean, screenshots, write page, SUBMIT (by ~H46).
```

### 3. Feature triage — decide fast, decide out loud

```text
For every feature ask, in order:
  1. Does the core loop work WITHOUT it?   -> if yes, it's a stretch goal, not MVP.
  2. Can a player tell it's missing?       -> if no, cut it.
  3. Is it < 30 min of work?               -> if no, defer past the ship buffer.
Default answer under deadline pressure is CUT. You can always add in a post-jam version.
```

### 4. Pre-submission build check (run on a clean copy, not your dev folder)

```text
[ ] Build runs from an extracted zip on a path with NO engine/IDE installed.
[ ] Controls are shown on-screen or on the page (jurors won't read your mind).
[ ] No dev console errors; no soft-lock; restart works.
[ ] Web build (if any) is set to the platform's playable-in-browser mode.
[ ] Page has: 1-line pitch, controls, screenshots, credits + asset licenses.
[ ] File uploaded and the submission is actually attached to the JAM, not just the page.
```

## Pitfalls

- **Scope creep is the #1 jam killer.** If the core loop isn't playable by the first third
  of the clock, cut features now, not later.
- **No ship buffer.** Exporting, zipping, and writing the page reliably takes 1-3 hours and
  always surfaces a build bug. Treat the deadline as ~2 hours earlier than it is.
- **Submitting to the page but not the jam.** On itch.io a jam entry is a separate
  *submission* linked from the jam page — uploading the game alone does not enter it.
- **Untested export.** "Works in the editor" is not "works in the build." Test the exported
  artifact on a clean path; missing assets and wrong working directories are classic.
- **Unlicensed assets.** Music/fonts/sprites pulled from the web can violate jam rules and
  break later distribution. Use assets you're licensed for and list them in the credits.
- **Polishing before the loop is fun.** Juice multiplies fun; it can't create it. Get the
  loop right with placeholders first.

## References

- For the throwaway-vs-keep prototyping mindset and greyboxing technique, read the
  `prototype-fast` skill.
- For the actual upload mechanics (project page, channels, `butler push`), read
  `itch-publish`.

## Related skills

- `prototype-fast` — validate a mechanic quickly before committing jam hours to it.
- `itch-publish` — create the page and upload the build (most jams are hosted on itch.io).
- Engine cores (`phaser-core`, `love2d-core`, `godot-gdscript`, …) and genre skills
  (`platformer`, `roguelike`, …) — build the actual loop the jam scopes around.
