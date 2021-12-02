from unittest import TestCase, main

from day_02 import part_1, part_2


class TestDay02(TestCase):
    _depths: list[str]

    def setUp(self):
        self._comands = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

    def test_part_1(self):
        self.assertEqual(part_1(self._comands), 150)

    def test_part_2(self):
        self.assertEqual(part_2(self._comands), 900)


if __name__ == '__main__':
    main()
