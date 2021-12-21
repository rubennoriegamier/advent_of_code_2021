from unittest import TestCase, main

from day_18 import reduce_snailfish_number, part_1, part_2


class TestDay18(TestCase):
    _snailfish_numbers: list[str]

    def setUp(self):
        self._snailfish_numbers = ['[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]',
                                   '[[[5,[2,8]],4],[5,[[9,9],0]]]',
                                   '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]',
                                   '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]',
                                   '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]',
                                   '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]',
                                   '[[[[5,4],[7,7]],8],[[8,3],8]]',
                                   '[[9,3],[[9,9],[6,[4,9]]]]',
                                   '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]',
                                   '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]']

    def test_reduce_snailfish_number(self):
        self.assertEqual(reduce_snailfish_number('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'),
                         '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')

    def test_part_1(self):
        self.assertEqual(part_1(self._snailfish_numbers), 4_140)

    def test_part_2(self):
        self.assertEqual(part_2(self._snailfish_numbers), 3_993)


if __name__ == '__main__':
    main()
