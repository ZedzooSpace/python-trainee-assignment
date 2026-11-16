import unittest
from matrix_spiral.spiral_traversal import traverse_counter_clockwise


class TestTraversal(unittest.TestCase):
    def test_empty(self) -> None:
        self.assertEqual(traverse_counter_clockwise([]), [])

    def test_1x1(self) -> None:
        self.assertEqual(traverse_counter_clockwise([[42]]), [42])

    def test_2x2(self) -> None:
        matrix = [
            [1, 2],
            [3, 4],
        ]
        self.assertEqual(traverse_counter_clockwise(matrix), [1, 3, 4, 2])

    def test_3x3(self) -> None:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertEqual(
            traverse_counter_clockwise(matrix),
            [1, 4, 7, 8, 9, 6, 3, 2, 5],
        )


if __name__ == "__main__":
    unittest.main()