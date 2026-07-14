import sys, os; sys.path.append(os.path.dirname(__file__))
from base import GodotBase
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Path to Godot project")
    args = parser.parse_args()
    GodotBase().run(["-e"], project=args.project, headless=False)

if __name__ == "__main__": main()
