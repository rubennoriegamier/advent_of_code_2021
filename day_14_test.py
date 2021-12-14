from unittest import TestCase, main

from day_14 import parse_insertion_rules, part_1, part_2


class TestDay14(TestCase):
    _template: str
    _insertion_rules: dict[str, str]

    def setUp(self):
        self._template = 'NNCB'
        self._insertion_rules = parse_insertion_rules('''
CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''.lstrip())

    def test_part_1(self):
        self.assertEqual(part_1(self._template, self._insertion_rules), 1_588)

    def test_part_2(self):
        self.assertEqual(part_2(self._template, self._insertion_rules), 2_188_189_693_529)


if __name__ == '__main__':
    main()
