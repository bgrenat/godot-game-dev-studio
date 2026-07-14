import os
import re
import sys

def analyze_rendering(project_path):
    print(f"--- Anara Insight: Rendering & Optimization (Elite) ---")
    print(f"Reference: See Anara Rubrics #3 (Rendering & VFX)")
    score = 70

    multimesh_chunks = 0
    particle_fallbacks = 0
    mesh_mi2d = 0
    
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.tscn'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Detect MeshInstance2D (Visionary for transparency)
                    mesh_mi2d += len(re.findall(r'type="MeshInstance2D"', content))
            
            if file.endswith('.gd'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Detect fallback logic for Compatibility renderer
                    if "get_current_renderer_type" in content or "gl_compatibility" in content.lower():
                        particle_fallbacks += 1

    score += (mesh_mi2d * 5)
    score += (particle_fallbacks * 15)

    score = max(0, min(100, score))
    print(f"Rendering Score: {score}/100")
    print(f"Notes: Found {mesh_mi2d} MeshInstance2D optimizations, {particle_fallbacks} renderer fallbacks.")
    return score

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    analyze_rendering(path)
