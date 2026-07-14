# Aurelius Protocol: Adapt Desktop To Mobile NEVER List

- **NEVER use mouse position directly** — Touch has no "hover" state. Replace mouse_motion with screen_drag and check InputEventScreenTouch.pressed.
- **NEVER keep small UI elements** — Apple HIG requires 44pt minimum touch targets. Android Material: 48dp. Scale up buttons 2-3x.
- **NEVER forget finger occlusion** — User's finger blocks 50-100px radius. Position critical info ABOVE touch controls, not below.
- **NEVER run at full performance when backgrounded** — Mobile OSs kill apps that drain battery in background. Pause physics, reduce FPS to 1-5 when app loses focus.
- **NEVER use desktop-only features** — Mouse hover, right-click, keyboard shortcuts, scroll wheel don't exist on mobile. Provide touch alternatives.
