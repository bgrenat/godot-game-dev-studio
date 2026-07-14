# Aurelius Protocol: Quest System NEVER List

- **NEVER store active quest data directly in the Player node** — If the player dies or the scene reloads, quest progress is lost. Use an AutoLoad or a persistent Data Resource [20].
- **NEVER use hardcoded string IDs for objectives without validation** — Typos in `update_objective("kill_slimes")` will fail silently. Use StringNames or a central ID registry [21].
- **NEVER forget to disconnect completion signals** — If a quest signal isn't cleared after completion, it might trigger multiple times, awarding double rewards [22].
- **NEVER poll for mission completion in `_process()`** — Checking objectives 60 times a second is wasteful. Use a signal-driven approach (e.g. `on_enemy_died`) [23].
- **NEVER skip save/load logic for quests** — Resetting a 10-hour quest line because of a game restart is a player-ending bug. Always persist quest states [24].
- **NEVER use `all()` on objective arrays without null/type checks** — Attempting to check completion on a null objective entry will crash the entire system [25].
- **NEVER hardcode quest logic inside enemy or item scripts** — Use a generic `EventBus` or `QuestTrigger` node to bridge the encounter to the QuestManager.
- **NEVER allow multiple instances of the same Quest Resource to be active** — Ensure you're tracking unique Quest IDs to prevent accidental duplication of missions.
- **NEVER use complex UI logic to calculate progress** — The UI should only display what the `Quest` resource provides. Keep formulas in the `QuestManager`.
- **NEVER award rewards directly inside the quest script** — Delegate reward distribution to the `InventoryManager` or `EconomyManager` via signals for decoupling.
