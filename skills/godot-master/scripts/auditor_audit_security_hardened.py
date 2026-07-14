import os
import re
import sys

def audit_security_hardened(project_path):
    print(f"--- Aurelius Protocol: Security & Hardening Audit (FATAL) ---")
    print(f"Reference: See Aurelius Encyclopedia #5.1 (RCE Vulnerabilities)")

    slop_count = 0
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.gd'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Fatal: Object decoding on untrusted data
                    if re.search(r'\.get_var\(\s*true\s*\)', content):
                        print(f"[!!!] FATAL SECURITY RISK in {file}: get_var(true) allows RCE.")
                        slop_count += 1
                        
                    if re.search(r'\.allow_object_decoding\s*=\s*true', content):
                        print(f"[!!!] FATAL SECURITY RISK in {file}: Object decoding enabled on MultiplayerAPI.")
                        slop_count += 1

    print(f"\nResult: {slop_count} instances of Security Slop found.")
    return slop_count

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_security_hardened(path)
