from unittest import TestCase, main

from day_15 import part_1, part_2


class TestDay15(TestCase):
    _risk_levels: list[list[int]]

    def setUp(self):
        self._risk_levels = [[1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
                             [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
                             [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
                             [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
                             [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
                             [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
                             [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
                             [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
                             [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
                             [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]]

    def test_part_1(self):
        self.assertEqual(part_1(self._risk_levels), 40)

    def test_part_2(self):
        self.assertEqual(part_2(self._risk_levels, 5), 315)


if __name__ == '__main__':
    main()
