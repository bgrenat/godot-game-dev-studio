import os
import re
import sys

def audit_nodes_bloat(project_path):
    print(f"--- Aurelius Protocol: Node Bloat & SceneTree Audit (Elite) ---")
    print(f"Reference: See Aurelius Encyclopedia #4.1 (Upward Structural Coupling)")

    slop_count = 0
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.tscn'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    node_count = content.count('[node name=')
                    if node_count > 500:
                        print(f"[!] COMPONENT BLOAT in {file}: Contains {node_count} nodes. Consider RefCounted/Resource for data.")
                        slop_count += 1
            
            if file.endswith('.gd'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    if content.count('get_parent()') > 3:
                        print(f"[!] COUPLING SLOP in {file}: Excessive use of get_parent(). Use signals upward.")
                        slop_count += 1

    print(f"\nResult: {slop_count} instances of Bloat/Coupling found.")
    return slop_count

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_nodes_bloat(path)
