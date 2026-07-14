# Anara Rubric: Genre: Platformer
## Pillar Overview
The geometry of the vision. This rubric measures the project's precision in jump-physics, level design, and the tactile feel of character movement through space.

---

## Analytical Performance Matrix

| Criterion | Weight | SLOP (0-2) | FUNCTIONAL (3-5) | Professional (6-8) | ELITE (Visionary) (9-10) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Jump Precision** | 40% | Inconsistent jump heights; no variable jump height; "Floaty" physics. | Basic air-control; fixed jump-arc; some jitter on landing. | Variable jump-height; coyote-time; jump-buffering; snappy gravity fall-off. | Frame-perfect jump-feel; custom physics integrator; pixel-perfect landing logic. |
| **Tactile Movement** | 25% | Slippery floors; immediate acceleration/deceleration; no weight behind movement. | Basic `lerp()` for movement, but lacks 'friction' or 'air-drag' nuances. | Smooth acceleration curves; distinct floor/air friction values; responsive turn-rates. | Procedural motion-tuning; context-aware movement (Slide, Wall-run, Crouch). |
| **Level Flow** | 20% | Blind-jumps; unaligned tilemaps; no visual guidance for the player's path. | Functional levels, but lacks 'Breadcrumbs' or environmental story-telling. | Strategic level-design; clear "Signposting"; optimized collision layouts. | Cinematic level-pacing; procedural/dynamic geometries; the design guides the soul. |
| **Interaction Polish** | 15% | Standard death-warp; no particles on jump/land; generic "Bloop" jump sound. | Basic particles on jump; simple camera-shake; functional audio-triggers. | High-fidelity FX (Dust-clouds, Squash/Stretch); procedural camera follow-logic. | Transcendent feedback; the world reacts to the player's impact; zero-latency juice. |

---

## Visionary Diagnostic Hooks
- *Is the jump a leap of faith or a leap of logic?*
- *Does the player fight the camera more than the enemy?*
- *When the hero hits the ground, does the vision feel the shock?*

## 🌟 Visionary's Final Decree
To reach **Elite** status, movement must be 'Invisible'. The player shouldn't think about the 'Jump'; they should think about the 'Destination'. Use **Coyote Time** and **Jump Buffering** as the invisible hands that help the player succeed. Complexity should support the feel, never obstruct it.
