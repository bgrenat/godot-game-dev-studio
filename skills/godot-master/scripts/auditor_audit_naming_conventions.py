import os
import re
import sys

def audit_naming_conventions(project_path):
    print(f"--- Aurelius Protocol: Naming Convention & Project Structure Audit ---")
    print(f"Target: {project_path}\n")

    issues_found = 0
    
    for root, _, files in os.walk(project_path):
        for file in files:
            # 1. Check for uppercase letters in file names (excluding C#)
            if not file.endswith('.cs') and re.search(r'[A-Z]', file):
                print(f"[!] SLOP DETECTED: File '{file}' contains uppercase letters.")
                print(f"    Expert Logic: Case-sensitivity causes fatal errors on Linux/Android exports. Use snake_case for all assets.\n")
                issues_found += 1
                
            # 2. Check GDScript files for naming violations
            if file.endswith('.gd'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Flag snake_case class names (should be PascalCase)
                    if re.search(r'class_name\s+[a-z_0-9]+', content):
                        print(f"[!] STYLE VIOLATION in {file}")
                        print(f"    Context: class_name is using snake_case.")
                        print(f"    Expert Logic: Class and Node names must be PascalCase as per the official style guide.\n")
                        issues_found += 1

    if issues_found == 0:
        print("Result: Project naming is cross-platform compliant.")
    else:
        print(f"Result: {issues_found} naming/style violations found.")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_naming_conventions(path)
