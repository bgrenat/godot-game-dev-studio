shader_type spatial;
render_mode blend_mix, depth_draw_opaque, cull_disabled;

## Expert Spectral Shader for downed/ghostly players.
## Simulates a translucent, glowing soul effect.

uniform vec4 ghost_color : source_color = vec4(0.4, 0.8, 1.0, 0.4);
uniform float glow_intensity : hint_range(0.0, 5.0) = 2.0;
uniform float wave_speed : hint_range(0.0, 10.0) = 1.0;

void fragment() {
	// Simple sine wave for "pulsing" soul effect
	float pulse = (sin(TIME * wave_speed) + 1.0) * 0.5;
	
	ALBEDO = ghost_color.rgb;
	ALPHA = ghost_color.a * (0.5 + pulse * 0.5);
	
	// Add emissive glow
	EMISSION = ghost_color.rgb * glow_intensity;
}
