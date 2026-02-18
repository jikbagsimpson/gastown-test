"""Tests for the hello world CLI."""

import subprocess
import sys
import unittest
from pathlib import Path

# Add src to path so we can import hello
SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

import hello


class TestGreet(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(hello.greet("World"), "Hello, World!")

    def test_custom_name(self):
        self.assertEqual(hello.greet("Alice"), "Hello, Alice!")

    def test_custom_greeting(self):
        self.assertEqual(hello.greet("Bob", "Hi"), "Hi, Bob!")


class TestMain(unittest.TestCase):
    def test_no_args(self):
        """main() with no args returns 0."""
        result = hello.main([])
        self.assertEqual(result, 0)

    def test_with_name(self):
        result = hello.main(["Alice"])
        self.assertEqual(result, 0)

    def test_with_greeting_flag(self):
        result = hello.main(["--greeting", "Hi", "Bob"])
        self.assertEqual(result, 0)


class TestCLI(unittest.TestCase):
    """Integration tests running the script as a subprocess."""

    def test_cli_default(self):
        result = subprocess.run(
            [sys.executable, str(SRC_DIR / "hello.py")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello, World!")

    def test_cli_with_name(self):
        result = subprocess.run(
            [sys.executable, str(SRC_DIR / "hello.py"), "Alice"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello, Alice!")

    def test_cli_with_greeting(self):
        result = subprocess.run(
            [sys.executable, str(SRC_DIR / "hello.py"), "--greeting", "Hi", "Bob"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hi, Bob!")

    def test_cli_version(self):
        result = subprocess.run(
            [sys.executable, str(SRC_DIR / "hello.py"), "--version"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("0.1.0", result.stdout)


if __name__ == "__main__":
    unittest.main()
