from unittest import TestCase, main

from day_11 import part_1, part_2


class TestDay11(TestCase):
    _energy_levels: list[list[int]]

    def setUp(self):
        self._energy_levels = [[5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
                               [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
                               [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
                               [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
                               [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
                               [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
                               [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
                               [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
                               [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
                               [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]]

    def test_part_1(self):
        self.assertEqual(part_1(self._energy_levels), 1_656)

    def test_part_2(self):
        self.assertEqual(part_2(self._energy_levels), 195)


if __name__ == '__main__':
    main()
