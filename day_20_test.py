from unittest import TestCase, main

from day_20 import parse_algorithm, parse_image, part_1_and_2


class TestDay20(TestCase):
    def setUp(self):
        self._algorithm = parse_algorithm(
            '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..'
            '##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##....'
            '..#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...#'
            '#.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#..'
            '....#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#')
        self._image = parse_image('''
#..#.
#....
##..#
..#..
..###'''.split())

    def test_part_1(self):
        self.assertEqual(part_1_and_2(self._algorithm, self._image, 2), 35)

    def test_part_2(self):
        self.assertEqual(part_1_and_2(self._algorithm, self._image, 50), 3_351)


if __name__ == '__main__':
    main()
