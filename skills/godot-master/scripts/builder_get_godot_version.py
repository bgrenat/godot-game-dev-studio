import sys, os; sys.path.append(os.path.dirname(__file__))
from base import GodotBase

def main():
    print(GodotBase().run(["--version"]).stdout.strip())

if __name__ == "__main__": main()
