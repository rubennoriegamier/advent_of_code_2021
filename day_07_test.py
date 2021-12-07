from unittest import TestCase, main

from day_07 import part_1, part_2


class TestDay07(TestCase):
    _xs: list[int]

    def setUp(self):
        self._xs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    def test_part_1(self):
        self.assertEqual(part_1(self._xs), 37)

    def test_part_2(self):
        self.assertEqual(part_2(self._xs), 168)


if __name__ == '__main__':
    main()
