import os
import re
import sys

def analyze_assets(project_path):
    print(f"--- Anara Insight: Asset Optimization Index ---")
    score = 75 # Base score

    vram_compressed = 0
    lossless_pixel = 0
    unoptimized_3d = 0
    
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.import'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    # VRAM Compressed (3D)
                    if 'compress/mode=2' in content:
                        vram_compressed += 1
                    # Lossless (Good for small textures/pixel art)
                    elif 'compress/mode=0' in content:
                        lossless_pixel += 1
                        # If a texture is large and lossless, it's unoptimized for 3D
                        if 'mipmaps/generate=true' in content:
                            unoptimized_3d += 1

    score += (vram_compressed * 2)
    score -= (unoptimized_3d * 10)

    score = max(0, min(100, score))
    print(f"Asset Score: {score}/100")
    print(f"Notes: Found {vram_compressed} VRAM-compressed assets, {unoptimized_3d} unoptimized 3D textures (using Lossless).")
    return score

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    analyze_assets(path)
