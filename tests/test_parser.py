import unittest

from matrix_spiral.exceptions import MatrixFormatError
from matrix_spiral.parser import parse_matrix


class TestParser(unittest.TestCase):
    def test_parse_valid_matrix(self) -> None:
        raw = """
        +----+----+
        | 10 | 20 |
        +----+----+
        | 30 | 40 |
        +----+----+
        """
        self.assertEqual(parse_matrix(raw), [[10, 20], [30, 40]])

    def test_parse_invalid_matrix(self) -> None:
        invalid_cases = [
            "",
            "+---+---+",
            "| 10 | 20 |\n| 30 |",
            "| 10 | abc |",
            "| -5 | 10 |\n| 20 | 30 |",
            "10 | 20",
        ]
        for invalid_raw in invalid_cases:
            with self.subTest(invalid_raw=invalid_raw):
                with self.assertRaises(MatrixFormatError):
                    parse_matrix(invalid_raw)


if __name__ == "__main__":
    unittest.main()