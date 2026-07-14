import sys, os; sys.path.append(os.path.dirname(__file__))
from base import GodotBase
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pid", type=int, help="Process ID to stop")
    args = parser.parse_args()
    import subprocess, platform
    if platform.system().lower() == 'windows': subprocess.run(["taskkill", "/F", "/PID", str(args.pid)])
    else: os.kill(args.pid, 9)

if __name__ == "__main__": main()
