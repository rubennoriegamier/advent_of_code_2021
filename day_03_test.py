from unittest import TestCase, main

from day_03 import part_1, part_2


class TestDay03(TestCase):
    _bin_numbers: list[str]

    def setUp(self):
        self._bin_numbers = ['00100', '11110', '10110', '10111', '10101', '01111',
                             '00111', '11100', '10000', '11001', '00010', '01010']

    def test_part_1(self):
        self.assertEqual(part_1(self._bin_numbers), 198)

    def test_part_2(self):
        self.assertEqual(part_2(self._bin_numbers), 230)


if __name__ == '__main__':
    main()
