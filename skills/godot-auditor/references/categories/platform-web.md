# Aurelius Protocol: Platform Web NEVER List

- **NEVER use FileAccess for persistent saves** — Browsers sandbox the filesystem. Standard `FileAccess` to `user://` is unreliable. Always use `JavaScriptBridge` for `localStorage` or `IndexedDB`.
- **NEVER assume localStorage is permanent** — Browsers may purge local storage if space is low. Always implement a cloud-save fallback for production titles.
- **NEVER use the Forward+ renderer** — Forward+ requires Vulkan features that are unstable in browsers. Use the **Compatibility** (WebGL 2.0) renderer for consistent 60 FPS.
- **NEVER block the browser event loop** — Long-running sync logic will cause the browser to prompt the user to "Kill the Page." Use `await` and background tasks.
- **NEVER ignore the COOP/COEP header requirement** — Multi-threading and `SharedArrayBuffer` will fail on many hosts unless cross-origin isolation is configured server-side.
- **NEVER forget to handle tab focus loss** — Audio playing in a hidden background tab is poor UX. Use `visibilitychange` to pause audio.
- **NEVER trigger Fullscreen/Mouse Lock without click** — Browsers block security-sensitive requests unless they are inside a direct user interaction event.
- **NEVER use absolute paths in HTML shells** — Use relative paths to ensure the game works when hosted in sub-directories.
