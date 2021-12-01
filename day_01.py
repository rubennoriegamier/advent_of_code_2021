import fileinput
from collections.abc import Iterable
from itertools import islice, pairwise, starmap, tee
from operator import lt
from typing import Iterator


def main():
    depths: list[int] = list(map(int, fileinput.input()))

    print(part_1(depths))
    print(part_2(depths))


def part_1(depths: Iterable[int]) -> int:
    return sum(starmap(lt, pairwise(depths)))


def part_2(depths: Iterable[int]) -> int:
    a: Iterator[int]
    b: Iterator[int]
    c: Iterator[int]

    a, b, c = tee(depths, 3)

    return part_1(map(sum, zip(a, islice(b, 1, None), islice(c, 2, None))))


if __name__ == '__main__':
    main()
