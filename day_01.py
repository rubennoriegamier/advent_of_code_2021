import fileinput
from functools import partial
from itertools import islice
from operator import lt, sub


def main():
    depths = list(map(int, fileinput.input()))

    print(part_1(depths))
    print(part_2(depths))


def part_1(depths):
    return sum(map(partial(lt, 0), map(sub, islice(depths, 1, None), depths)))


def part_2(depths):
    return part_1(list(map(sum, zip(depths, islice(depths, 1, None), islice(depths, 2, None)))))


if __name__ == '__main__':
    main()
