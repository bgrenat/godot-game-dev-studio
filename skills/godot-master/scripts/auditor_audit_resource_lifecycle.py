import os
import re
import sys

def audit_resource_lifecycle(project_path):
    print(f"--- Aurelius Protocol: Resource Lifecycle & RID Audit (Elite) ---")
    print(f"Reference: See Aurelius Encyclopedia #1.1 (RID Leaks)")

    slop_count = 0
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.gd'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Detect RID allocation without free (Low-level Server Slop)
                    # Pattern: var x = RenderingServer.mesh_create()
                    alloc_pattern = r'(?:var\s+)?(\w+)\s*.*=\s*(RenderingServer|PhysicsServer3D|PhysicsServer2D|RenderingDevice|CameraServer)\.\w+_create\b'
                    allocs = re.findall(alloc_pattern, content)
                    
                    for var_name, server in allocs:
                        free_pattern = rf'{server}\.free_rid\(\s*{var_name}\s*\)'
                        if not re.search(free_pattern, content):
                            print(f"[!] RID LEAK in {file}: Variable '{var_name}' created via {server} but never freed.")
                            slop_count += 1

                    # Detect LocalToScene slop on Shared Resources
                    if 'extends Resource' in content and 'resource_local_to_scene = true' not in content:
                        if 'var ' in content: # Heuristic for stateful resources
                            print(f"[!] SHARED STATE SLOP in {file}: Resource has state but not marked 'local_to_scene'.")
                            slop_count += 1

    print(f"\nResult: {slop_count} instances of Lifecycle Slop found.")
    return slop_count

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_resource_lifecycle(path)
