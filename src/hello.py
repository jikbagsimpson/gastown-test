#!/usr/bin/env python3
"""A simple hello world CLI using argparse."""

import argparse
import sys


def create_parser():
    """Create and return the argument parser."""
    parser = argparse.ArgumentParser(
        description="A simple hello world CLI."
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="World",
        help="Name to greet (default: World)",
    )
    parser.add_argument(
        "--greeting",
        default="Hello",
        help="Greeting to use (default: Hello)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="hello 0.1.0",
    )
    return parser


def greet(name, greeting="Hello"):
    """Return a greeting string."""
    return f"{greeting}, {name}!"


def main(argv=None):
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args(argv)
    print(greet(args.name, args.greeting))
    return 0


if __name__ == "__main__":
    sys.exit(main())
