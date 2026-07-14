import sys, os; sys.path.append(os.path.dirname(__file__))
from base import GodotBase
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Path to Godot project")
    parser.add_argument("--log", default="debug.log", help="Log file path")
    args = parser.parse_args()
    GodotBase().run(["-v", "--log-file", args.log], project=args.project)

if __name__ == "__main__": main()
