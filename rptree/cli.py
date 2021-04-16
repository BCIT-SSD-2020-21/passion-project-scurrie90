"""Adds Command Line Functionality, eliminating need for a Python shell session"""
# cli.py

import argparse
import pathlib
import sys

from . import __version__ 
from .rptree import DirectoryTree

def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist... closing")
        sys.exit
    tree = DirectoryTree(root_dir)
    tree.generate()

def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="Recursive Python Directory Tree Generator",
        epilog="Thanks for using Recursive Python Tree Generator",
    )
    parser.version = f"Recursive Python Tree v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting from the stated root. Default is parent"
    )
    return parser.parse_args()