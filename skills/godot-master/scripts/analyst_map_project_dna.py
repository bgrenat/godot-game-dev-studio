import os
import re
import sys

def map_project_dna(project_path):
    print(f"--- Anara Insight: DNA & Structural Integrity (Elite) ---")
    print(f"Reference: See Anara Rubrics #4 (Production Hardening)")
    score = 80

    group_usage = 0
    snake_case_files = 0
    total_files = 0
    
    for root, _, files in os.walk(project_path):
        for file in files:
            total_files += 1
            if not re.search(r'[A-Z]', file):
                snake_case_files += 1
            
            if file.endswith('.gd') or file.endswith('.tscn'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Detect SceneTree Groups (Standard decoupled communication)
                    group_usage += len(re.findall(r'add_to_group|is_in_group|get_nodes_in_group', content))

    if total_files > 0:
        casing_ratio = snake_case_files / total_files
        if casing_ratio < 0.9:
            score -= 20
            print("STRUCTURAL SLOP: Excessive uppercase filenames detected. Risk of Linux/Android failure.")

    score += (group_usage * 1) # Small bonus for group pattern

    score = max(0, min(100, score))
    print(f"DNA Score: {score}/100")
    print(f"Notes: {snake_case_files}/{total_files} files follow snake_case. {group_usage} group operations found.")
    return score

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    map_project_dna(path)
