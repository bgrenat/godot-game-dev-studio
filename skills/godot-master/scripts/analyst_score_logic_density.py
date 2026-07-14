import os
import re
import sys

def score_logic_density(project_path):
    print(f"--- Anara Insight: Logic Density & Complexity ---")
    score = 80 # Base score

    hot_loops = 0
    god_objects = 0
    
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.gd'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Heuristic for heavy match/if in process
                    if '_process' in content:
                        if content.count('if ') > 5 or content.count('match ') > 1:
                            hot_loops += 1
                    
                    # Heuristic for God-Objects (Autoloads with high method count)
                    if 'class_name' in content and content.count('func ') > 20:
                        god_objects += 1

    score -= (hot_loops * 10)
    score -= (god_objects * 15)

    score = max(0, min(100, score))
    print(f"Logic Density Score: {score}/100")
    print(f"Notes: Found {hot_loops} hot-loop complexity warnings, {god_objects} potential God-Objects.")
    return score

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    score_logic_density(path)
