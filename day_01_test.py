from unittest import TestCase, main

from day_01 import part_1, part_2


class TestDay01(TestCase):
    def setUp(self):
        self._depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    def test_part_1(self):
        self.assertEqual(part_1(self._depths), 7)

    def test_part_2(self):
        self.assertEqual(part_2(self._depths), 5)


if __name__ == '__main__':
    main()
