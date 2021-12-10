from unittest import TestCase, main

from day_10 import part_1, part_2


class TestDay10(TestCase):
    _lines: list[str]

    def setUp(self):
        self._lines = ['[({(<(())[]>[[{[]{<()<>>',
                       '[(()[<>])]({[<{<<[]>>(',
                       '{([(<{}[<>[]}>{[]{[(<()>',
                       '(((({<>}<{<{<>}{[]{[]{}',
                       '[[<[([]))<([[{}[[()]]]',
                       '[{[{({}]{}}([{[{{{}}([]',
                       '{<[[]]>}<{[{[{[]{()[[[]',
                       '[<(<(<(<{}))><([]([]()',
                       '<{([([[(<>()){}]>(<<{{',
                       '<{([{{}}[<[[[<>{}]]]>[]]']

    def test_part_1(self):
        self.assertEqual(part_1(self._lines), 26_397)

    def test_part_2(self):
        self.assertEqual(part_2(self._lines), 288_957)


if __name__ == '__main__':
    main()
