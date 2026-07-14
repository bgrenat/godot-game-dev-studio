# Roguelike generation, FOV, and loot (depth)

Algorithms behind the systems in `SKILL.md`. Engine-neutral pseudocode. For the noise/RNG
primitives and seeding, defer to `procedural-gen`; this file is the roguelike-specific glue.

## 1. Dungeon generation approaches

Pick by the *texture* you want. All must end with a **connectivity pass** (§2).

### Rooms-and-corridors (classic, readable)

```python
# Place non-overlapping rooms, then connect their centers with L-shaped tunnels.
rooms = []
for _ in range(MAX_ROOMS):
    r = random_rect(rng, min=4, max=10)
    if any(r.intersects(other.expand(1)) for other in rooms):
        continue                      # reject overlaps (expand by 1 to keep walls between)
    carve_room(map, r)
    if rooms:                         # connect to the previous room
        carve_h_then_v(map, rooms[-1].center, r.center, rng)
    rooms.append(r)
# First room = player spawn; last/farthest room = stairs down.
```

### BSP (binary space partition — tidy, building-like)

Recursively split the map rectangle into sub-rectangles; place one room per leaf; connect
sibling rooms as you unwind the recursion. Produces evenly distributed, non-overlapping rooms.

### Cellular automata (organic caves)

```python
# Random fill, then smooth: a cell becomes wall if most neighbors are walls.
fill_random(map, wall_chance=0.45, rng=rng)
for _ in range(4, 6):                 # 4–6 smoothing passes
    for cell in map:
        walls = count_wall_neighbors(map, cell)   # 8-neighborhood
        map[cell] = WALL if walls >= 5 else FLOOR
# Then keep only the largest connected floor region (discard isolated pockets).
```

### Drunkard's walk (cheap, winding)

Start at a point and random-walk, carving floor, until a target floor percentage is reached.
Guaranteed connected (one continuous path) but can be too snaky without tuning.

## 2. Connectivity (never skip this)

```python
# Flood-fill from the player's start; any walkable cell not reached must be connected or removed.
reached = flood_fill(map, player_start)
regions = find_disconnected_floor_regions(map, reached)
for region in regions:
    carve_corridor(map, nearest_cell(reached), nearest_cell(region), rng)
# Re-flood and assert: every floor cell is now reachable.
```

For caves, the common shortcut is to keep only the single largest region and discard the rest.

## 3. Field of view — symmetric shadowcasting

Properties you want: **symmetric** (if A sees B, B sees A), no blind spots, no flicker as the
player moves. Recursive shadowcasting scans the eight octants around the origin, tracking a
"shadow" of slopes blocked by walls:

```
for each of 8 octants:
    scan rows outward from the origin up to radius R
    track the visible slope range [start_slope, end_slope]
    when a wall is hit, recurse into the narrower slope range beyond it,
    and continue the current row with the reduced range
mark a cell visible if it lies within the current slope range and within R
```

Implementation notes:
- Transform each octant into a common coordinate frame so one routine handles all eight.
- Use a circular radius check (`dx*dx + dy*dy <= R*R`) for a round light, not a square.
- Cache `explored` separately; render explored-but-not-visible cells dimmed.

A symmetric variant ("symmetric shadowcasting") is simpler to reason about and avoids
single-cell asymmetries; prefer it if you implement from scratch.

## 4. Weighted, depth-scaled loot and spawn tables

```python
# A drop table is a list of (entry, weight). Weight is relative, not a probability.
goblin_loot = [
    ("nothing",      60),
    ("gold_small",   25),
    ("healing_potion", 10),
    ("rare_scroll",   5),
]
def roll(table, rng):
    total = sum(w for _, w in table)
    pick  = rng.range(0, total)        # [0, total)
    upto  = 0
    for entry, w in table:
        upto += w
        if pick < upto:
            return entry

# Depth scaling: shift weights toward stronger entries as depth increases,
# e.g. add depth-gated entries or multiply rare weights by a depth factor.
```

Design guidance:
- Keep "nothing"/common as the bulk of weight so rares stay exciting.
- Gate powerful items behind a minimum depth so early runs can't snowball.
- Separate **monster** spawn tables from **item** drop tables; both scale with depth.
- For "exactly one of" results use weighted pick; for "each may drop" iterate independent rolls.

## 5. Run vs. profile state (permadeath + meta-progression)

- **Run state** (current dungeon, HP, inventory, seed): lives only during the run. For *true*
  permadeath, delete or invalidate this save the moment it is loaded so it cannot be reloaded.
- **Profile state** (unlocked items/classes, high scores, achievements, currency): persists
  across deaths. This is what a roguelite spends on meta-progression.
- Keep them in separate files/sections so wiping a run never touches the profile (see
  `save-systems` for slot/versioning details).
