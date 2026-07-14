# Pattern: State Machine Transition Guard

Centralized logic to validate if a state transition is allowed based on the current state.

```gdscript
func can_transition_to(new_state: StringName) -> bool:
    match name:
        &"Dead": return false  # Terminal state
        &"Stunned": return new_state == &"Idle"  # Can only recover to Idle
        _: return true
```
