#!/usr/bin/env python3
"""
Python Gym CLI
Interactive Command Center for coding exercises, design patterns, and system design.

Usage:
  python gym.py test [all | leetcode | hackerrank | patterns | lld]
  python gym.py list
  python gym.py daily
  python gym.py stats
"""

import os
import sys
import random
import subprocess
import argparse
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent

TEST_SUITES = {
    "leetcode": "exercises/leetcode",
    "hackerrank": "exercises/hackerrank",
    "patterns": "design_patterns",
    "lld": "system_design/02_low_level_design_lld",
}


def find_testable_files(target_dir: Path):
    """Find all executable python files containing test cases."""
    testable = []
    if not target_dir.exists():
        return testable
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                testable.append(Path(root) / file)
    return testable


def run_tests(target: str = "all"):
    """Execute test suites with clean reporting."""
    print("=" * 60)
    print(f"Python Gym Test Runner -- Target: {target.upper()}")
    print("=" * 60)

    if target == "all":
        paths_to_check = [ROOT_DIR / rel for rel in TEST_SUITES.values()]
    elif target in TEST_SUITES:
        paths_to_check = [ROOT_DIR / TEST_SUITES[target]]
    else:
        print(f"Error: Unknown target '{target}'. Choose from: all, leetcode, hackerrank, patterns, lld")
        sys.exit(1)

    files_to_run = []
    for path in paths_to_check:
        files_to_run.extend(find_testable_files(path))

    passed = 0
    failed = []

    for file_path in sorted(files_to_run):
        rel_path = file_path.relative_to(ROOT_DIR)
        res = subprocess.run([sys.executable, str(file_path)], capture_output=True, text=True)

        if res.returncode == 0:
            print(f"  [PASS] {rel_path}")
            passed += 1
        else:
            print(f"  [FAIL] {rel_path}")
            failed.append((rel_path, res.stderr))

    print("-" * 60)
    print(f"Results: {passed} passed, {len(failed)} failed out of {len(files_to_run)} total.")
    print("=" * 60)

    if failed:
        print("\nFailures:")
        for path, err in failed:
            print(f"\n--- {path} ---")
            print(err.strip())
        sys.exit(1)
    else:
        print("All tests passed successfully! [OK]\n")


def list_curriculum():
    """List all available modules across the 4 pillars."""
    print("=" * 60)
    print("Python Gym -- Full Curriculum Overview")
    print("=" * 60)

    pillars = {
        "1. Theory & Core Python": "theory",
        "2. Algorithmic Exercises": "exercises",
        "3. Design Patterns": "design_patterns",
        "4. System Design": "system_design",
    }

    for pillar_name, rel_dir in pillars.items():
        dir_path = ROOT_DIR / rel_dir
        if not dir_path.exists():
            continue
        print(f"\n* {pillar_name} (`{rel_dir}/`)")
        for item in sorted(os.listdir(dir_path)):
            item_path = dir_path / item
            if item_path.is_dir() and not item.startswith("."):
                py_files = len(list(item_path.glob("**/*.py")))
                ipynb_files = len(list(item_path.glob("**/*.ipynb")))
                md_files = len(list(item_path.glob("**/*.md")))
                details = []
                if py_files:
                    details.append(f"{py_files} py")
                if ipynb_files:
                    details.append(f"{ipynb_files} notebooks")
                if md_files:
                    details.append(f"{md_files} docs")
                print(f"   |-- {item}/ ({', '.join(details)})")


def pick_daily_challenge():
    """Pick a random practice challenge for interview prep."""
    exercise_files = find_testable_files(ROOT_DIR / "exercises")
    pattern_files = find_testable_files(ROOT_DIR / "design_patterns")
    lld_files = find_testable_files(ROOT_DIR / "system_design/02_low_level_design_lld")

    all_challenges = exercise_files + pattern_files + lld_files
    if not all_challenges:
        print("No challenges found.")
        return

    chosen = random.choice(all_challenges)
    rel = chosen.relative_to(ROOT_DIR)

    print("=" * 60)
    print("Daily Interview Practice Challenge")
    print("=" * 60)
    print(f"File: {rel}")
    print(f"Run : python {rel}")
    print("-" * 60)
    print("Tip: Review the problem constraints, implement from scratch, and verify with unit tests!")
    print("=" * 60)


def show_stats():
    """Display quantitative statistics of the repository."""
    exercises = len(find_testable_files(ROOT_DIR / "exercises"))
    patterns = len(find_testable_files(ROOT_DIR / "design_patterns"))
    lld = len(find_testable_files(ROOT_DIR / "system_design/02_low_level_design_lld"))
    notebooks = len(list((ROOT_DIR / "theory").glob("**/*.ipynb")))
    hld_studies = len(list((ROOT_DIR / "system_design/03_high_level_design_hld").glob("*.md"))) - 1

    print("=" * 60)
    print("Python Gym Statistics & Interview Inventory")
    print("=" * 60)
    print(f"  * Theory Interactive Notebooks : {notebooks}")
    print(f"  * Algorithmic Coding Exercises : {exercises}")
    print(f"  * GoF Design Pattern Modules   : {patterns}")
    print(f"  * Low-Level Design (LLD) Specs : {lld}")
    print(f"  * High-Level Design Case Studies: {max(0, hld_studies)}")
    print(f"  * Total Runnable Unit Tests   : {exercises + patterns + lld}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Python Gym Command Center")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    test_parser = subparsers.add_parser("test", help="Run automated test suites")
    test_parser.add_argument(
        "target",
        nargs="?",
        default="all",
        choices=["all", "leetcode", "hackerrank", "patterns", "lld"],
        help="Target test suite (default: all)",
    )

    subparsers.add_parser("list", help="List all curriculum modules")
    subparsers.add_parser("daily", help="Pick a random daily interview problem")
    subparsers.add_parser("stats", help="Display gym statistics")

    args = parser.parse_args()

    if args.command == "test":
        run_tests(args.target)
    elif args.command == "list":
        list_curriculum()
    elif args.command == "daily":
        pick_daily_challenge()
    elif args.command == "stats":
        show_stats()
    else:
        # Default action
        show_stats()
        print("\nTip: Run 'python gym.py test' to execute all unit tests or 'python gym.py daily' for a random problem.")


if __name__ == "__main__":
    main()
