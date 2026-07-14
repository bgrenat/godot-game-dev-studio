import sys, os; sys.path.append(os.path.dirname(__file__))
from base import GodotBase
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", help="Root directory to search")
    args = parser.parse_args()
    for p in GodotBase().list_projects(args.root): print(p)

if __name__ == "__main__": main()
