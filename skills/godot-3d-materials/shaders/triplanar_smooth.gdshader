shader_type spatial;

/**
 * Expert Triplanar Smoothing Shader - Godot 4.6
 * Prevents texture stretching on procedural meshes or steep slopes by 
 * projecting from three axes in World Space.
 */

render_mode world_vertex_coords;

uniform sampler2D albedo_tex : source_color, filter_linear_mipmap_anisotropic, repeat_enable;
uniform float texture_scale = 1.0;
uniform float blend_sharpness = 4.0;

varying vec3 v_world_pos;
varying vec3 v_world_normal;

void vertex() {
	v_world_pos = VERTEX;
	v_world_normal = NORMAL;
}

void fragment() {
	// 1. Calculate Weights
	vec3 weights = abs(v_world_normal);
	weights = pow(weights, vec3(blend_sharpness));
	weights /= (weights.x + weights.y + weights.z);
	
	// 2. Project UVs
	vec2 uv_x = v_world_pos.zy * texture_scale;
	vec2 uv_y = v_world_pos.xz * texture_scale;
	vec2 uv_z = v_world_pos.xy * texture_scale;
	
	// 3. Sample and Blend
	vec3 samp_x = texture(albedo_tex, uv_x).rgb;
	vec3 samp_y = texture(albedo_tex, uv_y).rgb;
	vec3 samp_z = texture(albedo_tex, uv_z).rgb;
	
	ALBEDO = (samp_x * weights.x) + (samp_y * weights.y) + (samp_z * weights.z);
}
