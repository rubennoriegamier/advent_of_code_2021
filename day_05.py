import fileinput
from collections import namedtuple

import numpy as np
# noinspection PyProtectedMember
from numpy.lib.stride_tricks import as_strided

Point = namedtuple('Point', 'x, y')
Segment = namedtuple('Segment', 'a, b')


def main():
    segments = list(map(parse_segment, fileinput.input()))

    print(part_1(segments))
    print(part_2(segments))


def parse_point(raw_point: str) -> Point:
    return Point(*map(int, raw_point.split(',')))


def parse_segment(raw_segment: str) -> Segment:
    return Segment(*sorted(map(parse_point, raw_segment.split(' -> '))))


def count_overlapping_coordinates(segments: list[Segment], include_diagonals: bool) -> int:
    max_x = 0
    max_y = 0

    for segment in segments:
        max_x = max(max_x, segment.b.x)
        max_y = max(max_y, segment.a.y, segment.b.y)

    matrix = np.zeros((max_y + 1, max_x + 1), np.ubyte)

    for segment in segments:
        if segment.a.x == segment.b.x:
            matrix[segment.a.y:segment.b.y + 1, segment.a.x] += 1
        elif segment.a.y == segment.b.y:
            matrix[segment.a.y, segment.a.x:segment.b.x + 1] += 1
        elif include_diagonals:
            if segment.a.y < segment.b.y:
                window = matrix[segment.a.y:, segment.a.x:]
                as_strided(window, (segment.b.y - segment.a.y + 1,), (matrix.shape[1] + 1,))[:] += 1
            else:
                window = matrix[segment.b.y:, segment.b.x:]
                as_strided(window, (segment.a.y - segment.b.y + 1,), (matrix.shape[1] - 1,))[:] += 1

    return (matrix >= 2).sum()


def part_1(segments: list[Segment]) -> int:
    return count_overlapping_coordinates(segments, False)


def part_2(segments: list[Segment]) -> int:
    return count_overlapping_coordinates(segments, True)


if __name__ == '__main__':
    main()
