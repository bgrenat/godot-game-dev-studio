import os
import re
import sys

def score_scalability(project_path):
    print(f"--- Anara Insight: Scalability & Flow (Elite) ---")
    print(f"Reference: See Anara Rubrics #2 (Scalability & Componentization)")
    score = 60

    resource_singletons = 0
    blackboard_usage = 0
    god_objects = 0
    signal_bus_spam = 0
    
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.gd'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Detect God-Object Autoloads (Heuristic: massive node tracking)
                    if re.search(r'(var|@export var)\s+\w+\s*:\s*(Node|CharacterBody|Player)', content):
                        god_objects += 1
                    
                    # Detect Signal Bus spam
                    if "GlobalEventBus" in content or "SignalBus" in content:
                        signal_bus_spam += 1
                        
                    # Detect Resource-based Singletons (Visionary)
                    if "extends Resource" in content and "class_name" in content:
                        resource_singletons += 1

    score += (resource_singletons * 5)
    score -= (god_objects * 15)
    score -= (signal_bus_spam * 10)

    score = max(0, min(100, score))
    print(f"Scalability Score: {score}/100")
    print(f"Notes: Found {resource_singletons} Resource classes, {god_objects} God-Object risks.")
    return score

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    score_scalability(path)
