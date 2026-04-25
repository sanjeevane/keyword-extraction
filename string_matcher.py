"""Utilities for comparing strings and finding matches."""

from __future__ import annotations

import argparse
from collections import Counter
from typing import Iterable


def find_matching_strings(values: Iterable[str], *, case_sensitive: bool = True) -> dict[str, int]:
    """Return strings that appear more than once in *values*.

    Args:
        values: Any iterable containing string values to compare.
        case_sensitive: If ``False``, values are matched ignoring case.

    Returns:
        A dictionary mapping each matching string to its total count.
    """

    normalized_values = list(values)
    if not case_sensitive:
        normalized_values = [value.lower() for value in normalized_values]

    counts = Counter(normalized_values)
    return {value: count for value, count in counts.items() if count > 1}


def all_strings_match(values: Iterable[str], *, case_sensitive: bool = True) -> bool:
    """Return ``True`` if every provided value matches every other value."""

    normalized_values = list(values)
    if not normalized_values:
        return True

    if not case_sensitive:
        normalized_values = [value.lower() for value in normalized_values]

    first = normalized_values[0]
    return all(value == first for value in normalized_values)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare a set of strings and report matching values.",
    )
    parser.add_argument(
        "values",
        nargs="+",
        help="Strings to compare.",
    )
    parser.add_argument(
        "--ignore-case",
        action="store_true",
        help="Match strings without considering case.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    matches = find_matching_strings(args.values, case_sensitive=not args.ignore_case)
    every_value_matches = all_strings_match(args.values, case_sensitive=not args.ignore_case)

    if matches:
        print("Matching strings:")
        for value, count in sorted(matches.items()):
            print(f"- {value}: {count} occurrences")
    else:
        print("No repeated strings found.")

    print(f"All strings match: {every_value_matches}")


if __name__ == "__main__":
    main()
