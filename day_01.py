import fileinput
from collections.abc import Iterable, Iterator
from itertools import islice, pairwise, starmap, tee
from operator import lt


def main():
    depths: list[int] = list(map(int, fileinput.input()))

    print(part_1(depths))
    print(part_2(depths))


def part_1(depths: Iterable[int]) -> int:
    return sum(starmap(lt, pairwise(depths)))


def part_2(depths: Iterable[int]) -> int:
    a: Iterator[int]
    b: Iterator[int]

    a, b = tee(depths)

    return sum(map(lt, a, islice(b, 3, None)))


if __name__ == '__main__':
    main()
