import os
import re
import sys

def audit_circular_deps(project_path):
    print(f"--- Aurelius Protocol: Circular Dependency & Signal Loop Audit ---")
    print(f"Target: {project_path}\n")

    # Regex for property infinite loops (set(value): property = value)
    prop_loop_re = re.compile(r'var\s+(\w+).*?set\(value\):.*?(\1\s*=\s*value)', re.DOTALL)
    
    issues_found = 0
    
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.gd'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = prop_loop_re.finditer(content)
                    for match in matches:
                        line_num = content.count('\n', 0, match.start()) + 1
                        print(f"[!] SLOP DETECTED in {file}:{line_num}")
                        print(f"    Context: Property setter logic detected as an infinite loop.")
                        print(f"    Expert Logic: Assigning to a property inside its own setter triggers the setter recursively. Use a backing field (_property).\n")
                        issues_found += 1
                    
                    # Heuristic for signal emitting from its own callback (prone to loops)
                    if 'signal ' in content:
                        for signal_match in re.finditer(r'signal\s+(\w+)', content):
                            sig_name = signal_match.group(1)
                            if f'{sig_name}.emit' in content and f'_on_{sig_name}' in content:
                                # This is a very rough check, but flags common loop logic
                                print(f"[!] WARNING in {file}: Potential Signal Loop")
                                print(f"    Context: Signal '{sig_name}' emitted in a script that also handles its callback.")
                                print(f"    Expert Logic: Ensure that emitting '{sig_name}' doesn't trigger a recursive callback loop.\n")
                                issues_found += 1

    if issues_found == 0:
        print("Result: No direct circular logic detected.")
    else:
        print(f"Result: {issues_found} circularity risks found.")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_circular_deps(path)
