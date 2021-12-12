from unittest import TestCase, main

from day_12 import Connections, parse_connections, part_1, part_2


class TestDay12(TestCase):
    _examples: list[Connections]

    def setUp(self):
        self._examples = [parse_connections(['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']),
                          parse_connections(['dc-end', 'HN-start', 'start-kj', 'dc-start', 'dc-HN',
                                             'LN-dc', 'HN-end', 'kj-sa', 'kj-HN', 'kj-dc']),
                          parse_connections(['fs-end', 'he-DX', 'fs-he', 'start-DX', 'pj-DX', 'end-zg',
                                             'zg-sl', 'zg-pj', 'pj-he', 'RW-he', 'fs-DX', 'pj-RW',
                                             'zg-RW', 'start-pj', 'he-WI', 'zg-he', 'pj-fs', 'start-RW'])]

    def test_part_1(self):
        for i, (connections, paths) in enumerate(zip(self._examples, [10, 19, 226])):
            with self.subTest(i=i):
                self.assertEqual(part_1(connections), paths)

    def test_part_2(self):
        for i, (connections, paths) in enumerate(zip(self._examples, [36, 103, 3_509])):
            with self.subTest(i=i):
                self.assertEqual(part_2(connections), paths)


if __name__ == '__main__':
    main()
