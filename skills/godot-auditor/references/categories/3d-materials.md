# Aurelius Protocol: 3D Materials NEVER List

- **NEVER use separate metallic/roughness/AO textures** — Use ORM packing (1 RGB texture with Occlusion/Roughness/Metallic channels) to save texture slots and memory.
- **NEVER forget to enable normal_enabled** — Normal maps don't work unless you set `normal_enabled = true`. Silent failure is common.
- **NEVER use TRANSPARENCY_ALPHA for cutout materials** — Use TRANSPARENCY_ALPHA_SCISSOR or TRANSPARENCY_ALPHA_HASH instead. Full alpha blending is expensive and causes sorting issues.
- **NEVER set metallic = 0.5** — Materials are either metallic (1.0) or dielectric (0.0). Values between are physically incorrect except for rust/dirt transitions.
- **NEVER use emission without HDR** — Emission values > 1.0 only work with HDR rendering enabled in Project Settings.
- **NEVER use transparent materials for large environmental surfaces** — Transparent objects cannot rely on the Z-buffer for early fragment rejection, resulting in massive overdraw. If only a tiny part of a mesh is transparent, split the mesh into two surfaces: one opaque, one transparent.
- **NEVER create hundreds of slightly varied StandardMaterial3D resources if performance is dropping** — Godot minimizes GPU state changes by automatically reusing the underlying shader for materials that share the exact same configuration flags (checkboxes). Try to group your material configurations.
- **NEVER attempt to fix Z-fighting strictly by moving objects further apart** — Floating-point precision degrades over distance. To fix flickering textures, increase your Camera3D's `Near` plane property and decrease the `Far` property to compress the precision range.
- **NEVER use unique Material resources per MeshInstance3D** — This breaks draw call batching. Use 'Instance Uniforms' to vary parameters while keeping a single shared material.
- **NEVER use Decals on dynamic moving actors without a Cull Mask** — Bullet holes should not stick to the player's face as they walk over them. Mask out character layers.
