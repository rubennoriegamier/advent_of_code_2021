from unittest import TestCase, main

from day_23 import parse_positions, part_1, part_2


class TestDay23(TestCase):
    def setUp(self):
        self._aa, self._bb, self._cc, self._dd = parse_positions('''
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########''')

    def test_part_1(self):
        self.assertEqual(part_1(self._aa, self._bb, self._cc, self._dd), 12_521)

    def test_part_2(self):
        self.assertEqual(part_2(self._aa, self._bb, self._cc, self._dd), 44_169)


if __name__ == '__main__':
    main()
