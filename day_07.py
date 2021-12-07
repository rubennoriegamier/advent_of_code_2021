from collections.abc import Iterable
from functools import partial
from itertools import accumulate
from math import ceil, floor
from operator import sub
from statistics import mean, median


def main():
    xs = list(map(int, input().split(',')))

    print(part_1(xs))
    print(part_2(xs))


def part_1(xs: Iterable[int]) -> int:
    return sum(map(abs, map(partial(sub, round(median(xs))), xs)))


def part_2(xs: Iterable[int]) -> int:
    xs = sorted(xs)
    fuel_costs = list(accumulate(range(xs[-1] + 1)))
    mean_ = mean(xs)

    return min(sum(fuel_costs[abs(x - n)] for x in xs) for n in [ceil(mean_), floor(mean_)])


if __name__ == '__main__':
    main()
