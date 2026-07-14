import os
import re
import sys

def audit_node_access(project_path):
    print(f"--- Aurelius Protocol: Fragile Node Access Audit ---")
    print(f"Target: {project_path}\n")

    # Regex for get_parent() or upward paths
    fragile_access_re = re.compile(r'(\.get_parent\(\)|get_node\s*\(\s*["\']\.\./|["\']\.\./)')
    
    issues_found = 0
    
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.gd'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if fragile_access_re.search(line):
                            print(f"[!] SLOP DETECTED in {file}:{i+1}")
                            print(f"    Line: {line.strip()}")
                            print(f"    Expert Logic: Upward coupling (get_parent) breaks encapsulation. Use Signals to communicate up and Exports/Groups to find sibling systems.\n")
                            issues_found += 1

    if issues_found == 0:
        print("Result: Node access is strictly decoupled. Structural integrity confirmed.")
    else:
        print(f"Result: {issues_found} instances of Fragile Access found.")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_node_access(path)
