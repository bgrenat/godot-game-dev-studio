import os
import re
import sys

def score_documentation(project_path):
    print(f"--- Anara Insight: API Documentation Integrity ---")
    score = 50 # Base score

    docstrings = 0
    type_hinted_methods = 0
    export_groups = 0
    
    total_methods = 0
    
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.gd'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    docstrings += len(re.findall(r'##', content))
                    export_groups += len(re.findall(r'@export_group', content))
                    
                    methods = re.findall(r'func\s+\w+', content)
                    total_methods += len(methods)
                    type_hinted_methods += len(re.findall(r'func\s+\w+.*?\)\s*->', content))

    if total_methods > 0:
        score += (type_hinted_methods / total_methods * 30)
    score += (docstrings * 2)
    score += (export_groups * 5)

    score = max(0, min(100, score))
    print(f"Documentation Score: {score}/100")
    print(f"Notes: Found {docstrings} docstrings, {type_hinted_methods}/{total_methods} type-hinted methods, {export_groups} export groups.")
    return score

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    score_documentation(path)
