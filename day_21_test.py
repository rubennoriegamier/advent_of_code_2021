from unittest import TestCase, main

from day_21 import part_1, part_2


class TestDay21(TestCase):
    def setUp(self):
        self._p_1_pos = 4
        self._p_2_pos = 8

    def test_part_1(self):
        self.assertEqual(part_1(self._p_1_pos, self._p_2_pos), 739_785)

    def test_part_2(self):
        self.assertEqual(part_2(self._p_1_pos, self._p_2_pos), 444_356_092_776_315)


if __name__ == '__main__':
    main()
