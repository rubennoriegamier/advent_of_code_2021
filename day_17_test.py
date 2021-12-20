from unittest import TestCase, main

from day_17 import part_1, part_2


class TestDay17(TestCase):
    _x_start: int
    _x_end: int
    _y_start: int
    _y_end: int

    def setUp(self):
        self._x_start = 20
        self._x_end = 30
        self._y_start = -10
        self._y_end = -5

    def test_part_1(self):
        self.assertEqual(part_1(self._y_start), 45)

    def test_part_2(self):
        self.assertEqual(part_2(self._x_start, self._x_end, self._y_start, self._y_end), 112)


if __name__ == '__main__':
    main()
