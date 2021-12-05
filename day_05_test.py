from unittest import TestCase, main

from day_05 import Segment, parse_segment, part_1, part_2


class TestDay05(TestCase):
    _segments: list[Segment]

    def setUp(self):
        self._segments = list(map(parse_segment,
                                  ['0,9 -> 5,9',
                                   '8,0 -> 0,8',
                                   '9,4 -> 3,4',
                                   '2,2 -> 2,1',
                                   '7,0 -> 7,4',
                                   '6,4 -> 2,0',
                                   '0,9 -> 2,9',
                                   '3,4 -> 1,4',
                                   '0,0 -> 8,8',
                                   '5,5 -> 8,2']))

    def test_part_1(self):
        self.assertEqual(part_1(self._segments), 5)

    def test_part_2(self):
        self.assertEqual(part_2(self._segments), 12)


if __name__ == '__main__':
    main()
