from unittest import TestCase, main

from day_06 import part_1, part_2


class TestDay06(TestCase):
    _timers: list[int]

    def setUp(self):
        self._timers = [3, 4, 3, 1, 2]

    def test_part_1(self):
        self.assertEqual(part_1(self._timers), 5_934)

    def test_part_2(self):
        self.assertEqual(part_2(self._timers), 26_984_457_539)


if __name__ == '__main__':
    main()
