import sys, os; sys.path.append(os.path.dirname(__file__))
from base import GodotBase
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Path to project")
    parser.add_argument("script", help="Unit test script to run")
    args = parser.parse_args()
    
    gb = GodotBase()
    res = gb.run(["-s", gb.normalize(args.script)], project=args.project)
    print(res.stdout); print(res.stderr)

if __name__ == "__main__": main()
