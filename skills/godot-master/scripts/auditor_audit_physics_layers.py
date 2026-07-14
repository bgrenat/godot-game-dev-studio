import os
import re
import sys

def audit_physics_layers(project_path):
    print(f"--- Aurelius Protocol: Physics Layer & Collision Audit ---")
    print(f"Target: {project_path}\n")

    # Parses .tscn files for default layer/mask (1/1)
    layer_re = re.compile(r'collision_layer\s*=\s*1')
    mask_re = re.compile(r'collision_mask\s*=\s*1')
    
    issues_found = 0
    
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.tscn'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if layer_re.search(content) and mask_re.search(content):
                        print(f"[!] SLOP DETECTED in {file}")
                        print(f"    Context: Node is using default Collision Layer 1 and Mask 1.")
                        print(f"    Expert Logic: Leaving everything on Layer 1 forces the physics engine to calculate collisions for everything against everything. Professional projects use a strict Collision Matrix.\n")
                        issues_found += 1

    if issues_found == 0:
        print("Result: Collision matrix is defined and optimized.")
    else:
        print(f"Result: {issues_found} nodes using lazy physics defaults.")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_physics_layers(path)
