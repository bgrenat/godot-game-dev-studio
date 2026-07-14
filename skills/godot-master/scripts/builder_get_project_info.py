import sys, os; sys.path.append(os.path.dirname(__file__))
from base import GodotBase
import argparse, json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Path to Godot project")
    args = parser.parse_args()
    print(json.dumps(GodotBase().get_project_info(args.project)))

if __name__ == "__main__": main()
