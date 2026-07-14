import os
import re
import sys

def score_standardization(project_path):
    print(f"--- Anara Insight: Standard Compliance Score ---")
    score = 70 # Base score (generous for standard users)

    casing_violations = 0
    style_violations = 0
    
    for root, _, files in os.walk(project_path):
        for file in files:
            if not file.endswith('.cs') and re.search(r'[A-Z]', file):
                casing_violations += 1
            if file.endswith('.gd'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    if re.search(r'class_name\s+[a-z_0-9]+', content):
                        style_violations += 1

    score -= (casing_violations * 10)
    score -= (style_violations * 10)

    score = max(0, min(100, score))
    print(f"Standardization Score: {score}/100")
    print(f"Notes: Found {casing_violations} file casing issues, {style_violations} style guide violations.")
    return score

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    score_standardization(path)
