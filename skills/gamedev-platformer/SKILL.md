---
name: gamedev-platformer
description: "Imported awesome-gamedev-agent-skills guidance for platformer workflows in game development projects."
---
# Platformer

A playbook for 2D platformers — the run/jump controller "feel", level structure, hazards,
and goals. This is a **compositional** skill: it wires an engine movement skill, a tilemap
skill, and design skills into a working game. It does **not** re-teach physics or tilemaps;
it tells you what to build and how to make jumping feel good.

## When to use

- Use when building a side-scrolling or single-screen platformer, a "Mario-like" /
  "Celeste-like", or any game whose core verb is **jump between surfaces**.
- Use when a jump feels floaty, unresponsive, or "unfair" and you need feel fixes
  (coyote time, jump buffering, variable height, corner correction).

**When *not* to use:** top-down movement with no gravity → use the engine movement skill
directly. 3D first-person traversal → `fps-shooter`. Grid/turn movement → `roguelike`.
For the raw kinematic body API, use `godot-2d-movement` (or your engine's controller skill).

## Core loop

**Observe a gap/hazard → commit to a jump or move → land safely (or die) → reach the next
checkpoint/goal.** A platformer lives or dies on the *moment-to-moment* feel of that single
jump, repeated thousands of times. Tighten the controller first; everything else is content.

## Must-have systems

1. **Run/jump controller** — horizontal accel/decel, gravity, jump, with the feel aids below.
2. **Solid + one-way collision** — ground, walls, and "jump-through" platforms.
3. **Level geometry** — a tilemap or hand-placed colliders; the playable space.
4. **Hazards + death/respawn** — spikes, pits, enemies; reset to the last checkpoint.
5. **Checkpoints / level goal** — progress markers and a win condition (flag, door, exit).
6. **Camera** — follows the player with a deadzone and look-ahead, clamped to level bounds.
7. **Juice** — landing dust, squash/stretch, hit-stop, sound. Cheap, huge feel payoff.

## Design knobs (make the jump feel right)

Tune these by **outcome** (height in tiles, time to apex in seconds), not by raw numbers.

| Knob | Effect | Sane starting point |
|------|--------|---------------------|
| Max jump height | reach | 3–4 tiles |
| Time to apex | "weight"/snappiness | 0.30–0.40 s |
| Fall gravity multiplier | snappy, non-floaty fall | 1.5–2.0× rise gravity |
| Coyote time | jump just after leaving a ledge | 0.08–0.12 s (~5–7 frames @60) |
| Jump buffer | press just before landing still jumps | 0.10–0.15 s |
| Variable jump cut | tap = short hop, hold = full | cut upward velocity ×0.4–0.5 on release |
| Apex hang | brief float at the top for air control | reduce gravity ×0.5 near `|vy|`<threshold |
| Ground accel / friction | responsiveness vs. ice | reach top speed in 0.05–0.1 s |
| Corner correction | nudge past a ledge clipped by 1–2 px | nudge up to ~4 px sideways |

Derive gravity and jump velocity from the *feel* values rather than guessing — see Pattern 1.

## Patterns

### 1. Solve jump physics from height + time (not magic numbers)

```python
# Pseudocode. Pick the FEEL you want, then derive the physics. y-axis points DOWN.
# From kinematics: h = (g * t^2) / 2  and  v0 = g * t.
JUMP_HEIGHT   = 3.5 * TILE      # how high, in world units
TIME_TO_APEX  = 0.35            # seconds to reach the top

gravity       = (2 * JUMP_HEIGHT) / (TIME_TO_APEX ** 2)   # rising gravity
jump_velocity = -(2 * JUMP_HEIGHT) / TIME_TO_APEX         # negative = upward
fall_gravity  = gravity * 1.8   # heavier on the way down → less floaty
```

### 2. Coyote time + jump buffer + variable height (the feel core)

```python
# Pseudocode in the per-frame update. dt = seconds since last frame.
# Timers count DOWN; refresh coyote while grounded, buffer on a fresh press.
if on_floor:
    coyote_timer = COYOTE_TIME           # 0.1
if jump_pressed_this_frame:
    buffer_timer = JUMP_BUFFER           # 0.12
coyote_timer -= dt
buffer_timer -= dt

# A jump is allowed if we pressed recently AND were grounded recently.
if buffer_timer > 0 and coyote_timer > 0:
    velocity.y   = jump_velocity
    buffer_timer = 0
    coyote_timer = 0                     # consume both so we can't double-jump

# Variable height: releasing jump early while still rising cuts the arc short.
if jump_released_this_frame and velocity.y < 0:
    velocity.y *= 0.45

# Asymmetric gravity: snappier fall than rise.
g = fall_gravity if velocity.y > 0 else gravity
velocity.y += g * dt
```

### 3. One-way platforms

Solid from above, pass-through from below. Most engines expose a "one-way collision" flag on
the tile/collider; enable it and let the player **drop through** by disabling that collision
for a few frames when the player holds Down + Jump. Do not re-implement collision math.

## Pitfalls / failure modes

- **Per-frame movement not scaled by `dt`** → speed changes with frame rate. Every velocity
  integration and timer must use `dt`. (See `physics-tuning`.)
- **Floaty jumps** → symmetric gravity. Make fall gravity heavier than rise gravity.
- **"The jump didn't register"** → no input buffering. Buffer presses for ~0.1 s before landing.
- **"I fell off and couldn't jump"** → no coyote time. Allow a jump for ~0.1 s after leaving ground.
- **Sticking to walls / catching on tile seams** → use a single capsule/box collider, not
  per-tile colliders, and add corner correction.
- **Tunneling through floors at high speed** → enable continuous collision / smaller fixed
  timestep for fast bodies (see `physics-tuning`).
- **Camera snaps and induces nausea** → smooth/lerp the follow, add a deadzone, clamp to bounds.
- **Difficulty wall from bad teaching** → introduce one mechanic per area before combining them.

## Composition (build it from these skills)

- **Controller body:** `godot-2d-movement` (Godot `CharacterBody2D`); for other engines use
  the engine core + physics skill (`unity-physics`, `phaser-arcade-physics`, `pygame-core`).
- **Levels:** `godot-tilemap` / `unity-tilemap-2d` for geometry; `level-design` for layout,
  pacing, and teaching order.
- **Feel/physics:** `physics-tuning` for timestep, CCD, and stability.
- **Input:** `input-systems` for buffering, rebinding, and gamepad support.
- **Polish:** `audio-design` for SFX/music; the engine animation skill for squash/stretch.
- **Process:** `prototype-fast` to greybox the controller before building content.

## References

- For jump math derivation, a full feel-tuning table, corner correction, moving/one-way
  platforms, and camera follow, read `references/feel-tuning.md`.
