---
name: gamedev-prototype-fast
description: "Imported awesome-gamedev-agent-skills guidance for prototype-fast workflows in game development projects."
---
# Prototype Fast

Get a mechanic into a player's hands fast to learn whether it's worth building. The output of
a prototype is a **decision** (keep / kill / refactor), not a product. Optimize for learning
speed, and decide up front whether the code is throwaway or load-bearing.

## When to use

- Use when validating a single mechanic or "what if", building a vertical slice / MVP,
  greyboxing a level or interaction, or de-risking an idea before committing real time.
- Use when the user says "just get something playable", "is this fun?", or "rough it in".

**When *not* to use:** a timed competition with a deadline and a submission (use `game-jam`);
shipping or updating a real release (use `steam-publish` / `itch-publish`); building the
production version of a validated feature (use the engine/genre skill directly).

## Core workflow

1. **Write the one question.** State the single thing the prototype must answer, e.g.
   *"Is grappling-while-falling satisfying to control?"* If you have two questions, build two
   prototypes. A prototype that tests everything tests nothing.
2. **Decide throwaway vs keep — before you write code.** Throwaway (a *spike*): hard-code,
   no architecture, delete after. Keep: still rough, but folder/names you can grow. Most
   prototypes should be throwaway; pretending otherwise is how prototypes rot into the
   shipping codebase.
3. **Set a hard timebox** (30-90 min for a mechanic; one sitting for a slice) and a visible
   timer. The constraint is the point — it forces you to test the *core* idea, not the trim.
4. **Greybox everything non-essential.** Primitives for art (boxes, circles, capsules),
   built-in fonts, one debug sound or none. Spend zero minutes on anything the question
   doesn't depend on.
5. **Instrument for the question.** Add on-screen debug text / gizmos that show the thing you
   are judging (speed, distance, timing window). You're measuring, not decorating.
6. **Playtest immediately and honestly.** Play it yourself, then hand it to one other person
   without explaining the controls. Watch where they struggle.
7. **Make the call against your kill criteria** (below). Keep → schedule the real build and
   *rewrite*, don't promote the spike. Kill → log the lesson and move on. Refactor → narrow
   the question and spike again.

## Patterns

### 1. The prototype brief (fill this in before coding)

```text
QUESTION:     The one thing this must prove (binary if possible).
CORE VERB:    The single action the player repeats.
THROWAWAY?:   yes -> hard-code freely, delete after.  no -> minimal structure to grow.
TIMEBOX:      e.g. 60 min. Stop when it rings, even if unfinished.
KEEP IF:      observable signal that means "fun / worth building" (see kill criteria).
KILL IF:      observable signal that means "stop".
```

### 2. Greybox the core loop, fake everything else (engine-agnostic pseudocode)

```text
# Only the CORE VERB is real. Visuals are primitives; systems are stubs.
on update(dt):
    read_input()
    apply_core_mechanic(dt)        # the ONLY thing you're testing — make this feel right
    draw_primitive(player)         # a box. not a sprite. not animated.
    draw_debug_hud(speed, timing)  # show the numbers you're judging
    # enemies, menus, save, audio, art -> stubbed or absent until the verb proves out
```

### 3. Kill criteria — make the keep/kill call observable, not emotional

```text
KEEP when, with placeholder art:
  - a fresh player does the core verb on purpose within ~30s, unprompted, and
  - you (or they) repeat the loop "one more time" without being asked.
KILL when:
  - the verb only feels good after you explain it, or
  - making it fun needs systems far beyond the prototype's scope, or
  - you're adding art/levels to avoid admitting the verb is flat.
REFACTOR when one variable is clearly off (too slow, window too tight) -> retune, retest.
```

### 4. Containment: keep a spike out of the shipping codebase

```text
prototypes/<idea-name>/      # separate folder or project, never imported by main game
  - hard-coded values, single file ok, magic numbers welcome
  - committed on a throwaway branch (or not at all)
Rule: a "keep" decision authorizes a REWRITE in the real project, not a copy-paste of the
spike. Prototype code carries prototype assumptions; shipping it ships the assumptions.
```

## Pitfalls

- **Polishing too early.** Art, menus, and audio make a flat mechanic look finished and
  delay the verdict. Greybox until the verb is proven.
- **No kill criteria.** Without a written "kill if", every prototype "has potential" and
  nothing gets cut. Decide the signal *before* you're attached to the code.
- **Building systems instead of the mechanic.** Inventory, save/load, and settings are not
  the question. Stub them.
- **The spike becomes the product.** Throwaway code promoted to production is technical debt
  with a fun origin story. Rewrite on a keep.
- **Prototyping in the real codebase.** It tangles experiments with shipping systems and
  makes the spike expensive to delete. Use a separate folder/project.
- **Testing only yourself.** You know the controls and the intent. One uncoached outside
  player reveals more in two minutes than an hour of self-play.

## References

- For working under a hard external deadline and submitting, read the `game-jam` skill.
- For the engine-specific core loop you'll greybox in, read that engine's skill
  (`godot-gdscript`, `phaser-core`, `love2d-core`, `unity-csharp-scripting`, …).

## Related skills

- `game-jam` — same scope discipline applied to a timed competition with a submission.
- Engine cores and genre skills — where a "keep" decision gets rebuilt properly.
