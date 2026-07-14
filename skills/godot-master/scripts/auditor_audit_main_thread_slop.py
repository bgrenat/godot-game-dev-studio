import os
import re
import sys

def audit_main_thread_slop(project_path):
    print(f"--- Aurelius Protocol: Main-Thread Slop & Stall Audit (Elite) ---")
    print(f"Reference: See Aurelius Encyclopedia #2.2 (Server Sync Getters)")

    slop_count = 0
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.gd'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Detect Server Sync Getters (Fatal Frame Stalls)
                    sync_getters = [
                        r'RenderingServer\.texture_get_data',
                        r'RenderingDevice\.buffer_get_data',
                        r'PhysicsServer3D\.body_get_state'
                    ]
                    for pattern in sync_getters:
                        if re.search(pattern, content):
                            print(f"[!] SYNC STALL in {file}: Server getter called! Stalls the CPU until GPU flush.")
                            slop_count += 1

                    # Detect Mutex/Lock contention in hot loops
                    if re.search(r'(while|for).*?:[\s\S]*?\.lock\(\)', content):
                        print(f"[!] LOCK CONTENTION in {file}: Mutex locking inside a loop. Batch data before locking.")
                        slop_count += 1
                        
    print(f"\nResult: {slop_count} instances of Thread Slop found.")
    return slop_count

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_main_thread_slop(path)
