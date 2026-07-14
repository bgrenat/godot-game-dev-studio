# Aurelius Protocol: Genre Educational NEVER List

- NEVER punish failure with a "Game Over"; strictly use **"Try Again"** or **Contextual Hints** to ensure a safe, encouraging learning environment.
- NEVER separate learning from gameplay ("Chocolate-covered broccoli"); strictly ensure the **mechanic IS the learning** (e.g., math-based trajectory calc).
- NEVER use walls of text for instructions; strictly use **Show, Don't Tell** methods: interactive diagrams, non-verbal tutorials, or 3-second looping GIFs.
- NEVER skip **Spaced Repetition** logic; strictly ensure successfully answered questions reappear at increasing intervals to verify long-term retention.
- NEVER focus on failure; strictly prominently display **Mastery %**, **XP Bars**, and **Skill Trees** to motivate through visible progress.
- NEVER use static difficulty; strictly implement **Adaptive Scaling** to maintain the "Flow State" (target ~70% success rate).
- NEVER hardcode text into UI; strictly use **Translation Keys (PO files)** for internationalization and classroom localized support.
- NEVER force TTS without user consent; strictly provide an in-game toggle and respect OS-level screen reader settings.
- NEVER use absolute pixel positioning; strictly use the **Anchoring & Container** system for responsive scaling across tablets and classroom laptops.
- NEVER perform heavy data grading on the main thread; strictly use **WorkerThreadPool** to prevent UI freezes during automated assessments.
- NEVER forget to handle **IME updates**; strictly monitor `NOTIFICATION_OS_IME_UPDATE` for complex character input support (e.g., East Asian).
- NEVER ignore `mouse_filter` on overlays; strictly set to `PASS` to prevent invisible containers from silently consuming clicks.
- NEVER update static strings in `_process()`; strictly update labels ONLY on state change events to save mobile/tablet battery.
- NEVER embed sensitive database credentials in exports; strictly use **Environment Variables** or proxy APIs for student data security.
