# Engine detection — full project fingerprint

The router body carries the primary signal per engine; this file holds the **complete**
fingerprint table, the disambiguation rules, and the secondary signals. Detection is
**exclusive**: pick exactly one engine skill set (or "unknown" and use the fallback).

Scan for the highest-confidence signal and stop at the first match in this precedence order.

| # | Engine | Primary signal (project files) | Secondary signals | Skill set root |
|:-:|--------|--------------------------------|-------------------|----------------|
| 1 | Godot | `project.godot` | `*.tscn`, `*.gd`, `*.gdshader`, `*.tres`, `export_presets.cfg` | `skills/godot/` |
| 2 | Unreal | `*.uproject` | `Source/**/*.Build.cs`, `Config/Default*.ini`, `*.uasset`, `Content/` | `skills/unreal/` |
| 3 | Unity | `Assets/` **and** `ProjectSettings/ProjectVersion.txt` | `*.unity`, `*.prefab`, `*.asmdef`, `Packages/manifest.json` | `skills/unity/` |
| 4 | Bevy | `Cargo.toml` with a `bevy` dependency | `*.rs` with `App::new()` / `use bevy::prelude` | `skills/other-engines/bevy-ecs/` |
| 5 | Phaser | `package.json` dep `phaser` | `import Phaser`, `new Phaser.Game` | `skills/web-engines/phaser-core`, `skills/web-engines/phaser-arcade-physics` |
| 6 | PixiJS | `package.json` dep `pixi.js` | `import * as PIXI`, `new PIXI.Application` | `skills/web-engines/pixijs-rendering/` |
| 7 | three.js | `package.json` dep `three` | `import * as THREE`, `*.gltf` / `*.glb` | `skills/web-engines/threejs-scene-setup`, `threejs-gltf-loading`, `threejs-materials-lighting` |
| 8 | LÖVE | `conf.lua`, or `main.lua` calling `love.*` | `*.love` | `skills/other-engines/love2d-core/` |
| 9 | pygame | `*.py` with `import pygame` | `pygame.init()`, `pygame.display.set_mode` | `skills/other-engines/pygame-core/` |
| 10 | Roblox | `*.rbxl` / `*.rbxlx`, or `*.project.json` (Rojo) | `*.luau`, `DataStoreService`, `game:GetService` | `skills/other-engines/roblox-luau`, `roblox-datastores` |

## Disambiguation rules (must-handle ambiguities)

- **Godot C# vs Unity vs Bevy** — all may contain a `.csproj` or `Cargo.toml`. The presence of
  `project.godot` means **Godot** (route `godot-csharp` for C# work) even when a `.csproj`
  exists. Unity requires the `Assets/` + `ProjectSettings/` pair, not just any `.cs`. Bevy
  requires a `bevy` dependency, not just any Rust crate.
- **Multiple web deps** — a `package.json` may list more than one of `phaser` / `pixi.js` /
  `three`. Prefer the library actually imported in the file under discussion; if unclear, ask
  which renderer the task targets before loading a web-engine skill.
- **Monorepo / multiple engines** — if more than one engine fingerprint is present, route by the
  file or subdirectory the request is about. If still ambiguous, ask one targeted question.
- **No engine files at all** — go to the unknown-engine fallback (router body §6). Many
  discipline / genre / workflow tasks need no engine at all.

## Plain-text engine mentions

If there are no project files but the request names an engine in prose ("in Unity", "using
Phaser", "a Godot game"), adopt that engine. Never load an engine skill on a guess when neither
a file signal nor a named engine is present.

## Confidence boosters from task files

Some non-project files raise confidence about the *task* (not the engine):

- `*.yarn` / `*.ink` → `dialogue-systems` (and `visual-novel` if the whole game is one).
- `steam_appid.txt` / Steamworks SDK → `steam-publish`.
- `.itch.toml` / `butler` usage → `itch-publish`.
- `*.inputactions` → `unity-input-system`; `IA_`/`IMC_` assets → `unreal-enhanced-input`.
- `NavMesh.asset` / baked navmesh → `unity-navmesh`; `BT_`/`BB_` assets → `unreal-behavior-trees`.
