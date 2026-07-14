# Platformer feel tuning (depth)

Deeper detail behind the controller in `SKILL.md`. All snippets are engine-neutral
pseudocode; the math is standard kinematics and ports to any engine. Tune by *outcome*
(tiles of height, seconds to apex), then read off the physics values.

## 1. Deriving jump physics

A jump is just projectile motion. Choose the two values a designer can actually feel —
**peak height** `h` and **time to reach the peak** `t` — and solve for the rest. With the
y-axis pointing down (most 2D engines):

```
gravity        g  = 2h / t²
jump_velocity  v0 = -2h / t          # negative = upward
peak reached after t seconds; total airtime ≈ 2t (symmetric gravity)
```

Asymmetric gravity makes the fall snappier than the rise without changing peak height:

```
rise_gravity = g
fall_gravity = g * fall_multiplier   # 1.5–2.0 feels good
# airtime shortens; the arc looks like a fast, weighty drop after a quick pop up.
```

If you instead know the jump velocity and want the height: `h = v0² / (2g)`.

## 2. Full feel knob reference

| Knob | What it changes | Typical range | Notes |
|------|-----------------|---------------|-------|
| Jump height | vertical reach | 2–5 tiles | Keep below the player's *commit* comfort. |
| Time to apex | weight/snappiness | 0.25–0.45 s | Lower = snappier, "tighter". |
| Fall multiplier | floatiness on descent | 1.3–2.2× | The single biggest "feel" lever. |
| Coyote time | post-ledge grace | 0.05–0.15 s | ~3–9 frames at 60 Hz. |
| Jump buffer | pre-land grace | 0.08–0.18 s | Forgive early presses. |
| Variable-jump cut | tap vs hold height | ×0.3–0.6 of vy | Cut only while rising. |
| Apex hang | air control at top | ×0.4–0.6 g near apex | Define apex as `|vy| < hang_threshold`. |
| Max fall speed | terminal velocity | clamp | Prevents tunneling and runaway speed. |
| Ground accel | time to top speed | 0.03–0.12 s | Instant = arcadey; longer = momentum. |
| Air control | steering mid-jump | 0.5–1.0× ground | <1 gives committed arcs. |
| Coyote-after-jump lockout | prevents double jumps | consume timers | Zero both timers on jump. |

## 3. Apex hang and fast-fall

```python
# Reduced gravity near the apex gives a moment of extra air control ("hang time").
if abs(velocity.y) < APEX_THRESHOLD and not on_floor:
    g = g * 0.5

# Optional fast-fall: holding Down past the apex increases downward gravity.
if holding_down and velocity.y > 0:
    g = g * 1.5
```

## 4. Corner correction (ceiling and ledge nudging)

When a rising jump clips a corner by a pixel or two, players read it as the game being
"sticky". Nudge them past it instead of stopping the jump dead:

```python
# On hitting a ceiling while rising, if only the outer 1–4 px are blocked,
# shift the body sideways into the free space and keep the upward velocity.
if blocked_overhead and velocity.y < 0:
    for offset in (1, 2, 3, 4):            # check small horizontal nudges
        if free_at(position + sideways * offset):
            position += sideways * offset
            break                          # keep rising; don't zero velocity.y
```

The same idea on landing edges (a few px of "ledge grab"/snap) makes platforms feel generous.

## 5. One-way platforms and drop-through

- Mark the platform's collision as one-directional (solid only when the player is above and
  moving down). Engines expose this directly — do not hand-roll it.
- **Drop-through:** when the player holds Down + Jump on a one-way platform, disable that
  collision for ~0.1–0.2 s (or until the player's top passes below the platform), then re-enable.

## 6. Moving platforms

- Carry the player: add the platform's per-frame delta to the player's position while standing
  on it, so they ride it instead of sliding off.
- Apply the platform's velocity to the player on jump-off so leaps from a moving platform feel
  physical. Cap the inherited horizontal velocity so it can't fling the player uncontrollably.

## 7. Camera follow

- **Deadzone:** a rectangle the player can move within before the camera reacts; stops jitter.
- **Look-ahead:** offset the camera target in the direction of motion / facing so the player
  sees what's coming. Lerp the offset; don't snap it.
- **Smoothing:** move the camera toward its target with an exponential `lerp(cam, target,
  1 - exp(-k*dt))` rather than a fixed fraction, so it is frame-rate independent.
- **Clamp:** keep the camera rect inside the level bounds so you never show out-of-level space.
- **Vertical care:** lock or slow vertical follow during normal jumps; only follow Y on large
  height changes (falling into a pit, climbing) to avoid bobbing on every hop.

## 8. Teaching and pacing (hand-off to `level-design`)

- Introduce one mechanic in isolation, let the player practice it safely, *then* combine it
  with a known one. Never introduce two new things in the same hazard.
- Place the first instance of any lethal hazard where failure is cheap (near a checkpoint,
  no long re-traversal).
- Keep checkpoint-to-checkpoint segments short early, longer later; respawn must be instant.
