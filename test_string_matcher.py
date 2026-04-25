import unittest

from string_matcher import all_strings_match, find_matching_strings


class StringMatcherTests(unittest.TestCase):
    def test_find_matching_strings_returns_duplicates(self) -> None:
        values = ["apple", "banana", "apple", "pear", "banana", "banana"]
        self.assertEqual(find_matching_strings(values), {"apple": 2, "banana": 3})

    def test_find_matching_strings_respects_case_mode(self) -> None:
        values = ["Red", "red", "BLUE"]
        self.assertEqual(find_matching_strings(values), {})
        self.assertEqual(find_matching_strings(values, case_sensitive=False), {"red": 2})

    def test_all_strings_match(self) -> None:
        self.assertTrue(all_strings_match(["x", "x", "x"]))
        self.assertFalse(all_strings_match(["x", "y"]))

    def test_all_strings_match_ignore_case(self) -> None:
        self.assertTrue(all_strings_match(["Hello", "hello"], case_sensitive=False))


if __name__ == "__main__":
    unittest.main()
