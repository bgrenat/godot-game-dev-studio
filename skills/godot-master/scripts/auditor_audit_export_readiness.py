import os
import re
import sys

def audit_export_readiness(project_path):
    print(f"--- Aurelius Protocol: Export Readiness & UID Audit (Elite) ---")
    print(f"Reference: See Aurelius Encyclopedia #5.2 (Case-Sensitivity)")

    slop_count = 0
    
    # 1. Check for Case-Sensitivity (Snake Case enforcement)
    for root, _, files in os.walk(project_path):
        for file in files:
            if re.search(r'[A-Z]', file) and not file.endswith('.cs'):
                print(f"[!] EXPORT RISK in {file}: Uppercase in filename. Crashes on Linux/Android.")
                slop_count += 1

    # 2. Check for UID Collisions in .tscn
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.tscn'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    uids = re.findall(r'id="([a-zA-Z0-9_]+)"', content)
                    if len(uids) != len(set(uids)):
                        print(f"[!] UID COLLISION in {file}: Duplicate internal IDs found.")
                        slop_count += 1

    print(f"\nResult: {slop_count} instances of Export Slop found.")
    return slop_count

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_export_readiness(path)
