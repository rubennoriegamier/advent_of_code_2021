from unittest import TestCase, main

from day_09 import part_1, part_2


class TestDay09(TestCase):
    _heights: list[list[int]]

    def setUp(self):
        self._heights = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                         [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                         [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                         [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                         [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]

    def test_part_1(self):
        self.assertEqual(part_1(self._heights), 15)

    def test_part_2(self):
        self.assertEqual(part_2(self._heights), 1_134)


if __name__ == '__main__':
    main()
