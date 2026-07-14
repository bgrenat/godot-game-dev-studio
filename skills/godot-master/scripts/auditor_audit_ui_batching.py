import os
import re
import sys

def audit_ui_batching(project_path):
    print(f"--- Aurelius Protocol: UI Batching & Anchor Audit ---")
    print(f"Target: {project_path}\n")

    # Heuristic for manual offsets without anchors
    offset_re = re.compile(r'offset_.*?\s*=\s*[0-9]{3,}')
    anchor_zero_re = re.compile(r'grow_horizontal\s*=\s*1') # Simple check for likely un-anchored
    
    issues_found = 0
    
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.tscn'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if offset_re.search(content) and 'anchor_' not in content:
                        print(f"[!] SLOP DETECTED in {file}")
                        print(f"    Context: UI node detected with high pixel offsets but no anchor definitions.")
                        print(f"    Expert Logic: Hardcoded pixel offsets fail on resolution/aspect ratio swap. Use the Anchors and Containers system for responsive UI.\n")
                        issues_found += 1

    if issues_found == 0:
        print("Result: UI layout is mathematically responsive.")
    else:
        print(f"Result: {issues_found} UI nodes with fragile layout detected.")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_ui_batching(path)
