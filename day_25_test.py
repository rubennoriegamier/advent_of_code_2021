from unittest import TestCase, main

from day_25 import parse_seafloor_map, part_1


class TestDay25(TestCase):
    def setUp(self):
        self._seafloor_map = parse_seafloor_map(['v...>>.vv>',
                                                 '.vv>>.vv..',
                                                 '>>.>v>...v',
                                                 '>>v>>.>.v.',
                                                 'v>v.vv.v..',
                                                 '>.>>..v...',
                                                 '.vv..>.>v.',
                                                 'v.v..>>v.v',
                                                 '....v..v.>'])

    def test_part_1(self):
        self.assertEqual(part_1(self._seafloor_map), 58)


if __name__ == '__main__':
    main()
