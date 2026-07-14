# Aurelius Protocol: Adapt 2D To 3D NEVER List

- **NEVER directly replace Vector2 with Vector3(x, y, 0)** — This creates a "flat 3D" game with no depth gameplay. Add Z-axis movement or camera rotation to justify 3D.
- **NEVER keep 2D collision layers** — 2D and 3D physics use separate layer systems. You must reconfigure collision_layer/collision_mask for 3D nodes.
- **NEVER forget to add lighting** — 3D without lights is pitch black (unless using unlit materials). Add at least one DirectionalLight3D.
- **NEVER use Camera2D follow logic in 3D** — Camera3D needs spring arm or look-at logic. Direct position copying causes clipping and disorientation.
- **NEVER assume same performance** — 3D is 5-10x more demanding. Budget for lower draw calls, smaller viewport resolution on mobile.
- **NEVER use the rotation property for complex 3D logic** — 3D rotation uses Euler angles. Interpolating Euler angles causes unpredictable paths and Gimbal Lock. Always use `Quaternion` for 3D rotation interpolation or the `Basis` matrix for directional vectors.
- **NEVER ignore metric scaling** — 3D physics and lighting assume 1 unit = 1 meter. Scaling models inside the engine introduces precision errors. Export assets from DCCs at the correct metric scale.
- **NEVER disable physics interpolation when using custom camera follow scripts** — Updating camera position in `_process` to follow a body moving in `_physics_process` causes jitter. Use `Node3D.get_global_transform_interpolated()` for smooth transforms.
