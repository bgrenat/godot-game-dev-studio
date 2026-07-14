import sys, os; sys.path.append(os.path.dirname(__file__))
from base import GodotBase
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Path to project")
    parser.add_argument("preset", help="Export preset name")
    parser.add_argument("out", help="Output path")
    args = parser.parse_args()
    
    gb = GodotBase()
    res = gb.run(["--export-release", args.preset, gb.normalize(args.out)], project=args.project)
    print(res.stdout); print(res.stderr)

if __name__ == "__main__": main()
