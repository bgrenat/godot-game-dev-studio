import os
import re
import sys

def audit_shader_efficiency(project_path):
    print(f"--- Aurelius Protocol: Shader Efficiency & VGPR Audit (Elite) ---")
    print(f"Reference: See Aurelius Encyclopedia #3.1 (Batching Breakers)")

    slop_count = 0
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.gdshader'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Detect Dynamic Branching (VGPR pressure slop)
                    if re.search(r'^\s*if\s*\(', content, re.MULTILINE):
                        print(f"[!] SHADER SLOP in {file}: Dynamic 'if' detected. Use '#if' preprocessor for static toggles.")
                        slop_count += 1
                    
                    # Detect Unused Uniforms (Warning)
                    uniforms = re.findall(r'uniform\s+\w+\s+(\w+)', content)
                    for u in uniforms:
                        if content.count(u) == 1:
                            print(f"[!] UNUSED UNIFORM in {file}: '{u}' is declared but never used.")
                            slop_count += 1

    print(f"\nResult: {slop_count} instances of Shader Slop found.")
    return slop_count

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_shader_efficiency(path)
