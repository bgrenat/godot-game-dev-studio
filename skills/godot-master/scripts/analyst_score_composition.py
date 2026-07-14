import os
import re
import sys

def score_composition(project_path):
    print(f"--- Anara Insight: Composition Depth Score ---")
    score = 60 # Base score

    component_nodes = 0
    inheritance_depths = 0
    
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.gd'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Heuristic for component nodes (Scene child nodes with their own scripts)
                    component_nodes += len(re.findall(r'(\w+Component\.gd)', content))
                    
                    # Heuristic for inheritance (extends beyond base node)
                    extends_match = re.search(r'extends\s+(\w+)', content)
                    if extends_match and extends_match.group(1) not in ['Node', 'Node2D', 'Node3D', 'Control', 'RefCounted', 'Resource']:
                        inheritance_depths += 1

    score += (component_nodes * 5)
    score -= (inheritance_depths * 10)

    score = max(0, min(100, score))
    print(f"Composition Score: {score}/100")
    print(f"Notes: Found {component_nodes} actor components, {inheritance_depths} deep inheritance chains.")
    return score

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    score_composition(path)
