import os
import re
import sys

def audit_type_safety(project_path):
    print(f"--- Aurelius Protocol: Type Safety & Container Audit (Elite) ---")
    print(f"Reference: See Aurelius Encyclopedia #1.2 (RefCounted Circularity Risks)")

    slop_count = 0
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.gd'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Detect untyped arrays/dictionaries (Variant Slop)
                    untyped_patterns = [
                        (r'var\s+\w+\s*=\s*\[\]', "Untyped Array detected. Use 'Array[Type]' for VM speed."),
                        (r'var\s+\w+\s*=\s*\{\}', "Untyped Dictionary detected. Use 'Dictionary[Key, Value]' in 4.x.")
                    ]
                    
                    for pattern, msg in untyped_patterns:
                        matches = re.finditer(pattern, content)
                        for m in matches:
                            print(f"[!] TYPE SLOP in {file}: {msg}")
                            slop_count += 1

                    # Detect missing @export type hints
                    if re.search(r'@export\s+var\s+\w+\s*[^\:]*$', content, re.MULTILINE):
                        print(f"[!] EXPORT SLOP in {file}: Missing type hint on @export. Forces slow Variant boxing.")
                        slop_count += 1

    print(f"\nResult: {slop_count} instances of Type Slop found.")
    return slop_count

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_type_safety(path)
