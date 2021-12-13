from unittest import TestCase, main

from day_13 import Dot, Fold, parse_dots, parse_folds, part_1


class TestDay13(TestCase):
    _dots: list[Dot]
    _folds: list[Fold]

    def setUp(self):
        raw_dots, raw_folds = '6,10\n0,14\n9,10\n0,3\n10,4\n4,11\n6,0\n6,12\n4,1\n0,13\n10,12\n3,4\n3,0\n8,4\n1,10\n' \
                              '2,14\n8,10\n9,0\n\nfold along y=7\nfold along x=5'.split('\n\n')
        self._dots = parse_dots(raw_dots)
        self._folds = parse_folds(raw_folds)

    def test_part_1(self):
        self.assertEqual(part_1(self._dots, self._folds), 17)


if __name__ == '__main__':
    main()
