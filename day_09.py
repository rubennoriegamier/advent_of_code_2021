import fileinput
from bisect import insort
from functools import partial

import numpy as np


def main():
    heights: list[list[int]] = list(map(list, map(partial(map, int), map(str.rstrip, fileinput.input()))))

    print(part_1(heights))
    print(part_2(heights))


def part_1(heights: list[list[int]]) -> int:
    heights_ = np.asarray(heights, np.byte)
    mask = np.ones_like(heights_, bool)

    np.less(heights_[1:], heights_[:-1], out=mask[1:], where=mask[1:])
    np.less(heights_[:, 1:], heights_[:, :-1], out=mask[:, 1:], where=mask[:, 1:])
    np.less(heights_[:, :-1], heights_[:, 1:], out=mask[:, :-1], where=mask[:, :-1])
    np.less(heights_[:-1], heights_[1:], out=mask[:-1], where=mask[:-1])

    heights_ += 1

    return heights_.sum(where=mask)


def part_2(heights: list[list[int]]) -> int:
    heights_ = np.asarray(heights, np.byte)
    mask = np.ones_like(heights_, bool)

    np.less(heights_[1:], heights_[:-1], out=mask[1:], where=mask[1:])
    np.less(heights_[:, 1:], heights_[:, :-1], out=mask[:, 1:], where=mask[:, 1:])
    np.less(heights_[:, :-1], heights_[:, 1:], out=mask[:, :-1], where=mask[:, :-1])
    np.less(heights_[:-1], heights_[1:], out=mask[:-1], where=mask[:-1])

    max_y = heights_.shape[0] - 1
    max_x = heights_.shape[1] - 1
    sizes = []

    for y, x in zip(*np.nonzero(mask)):
        mask[y, x] = False
        size = 0
        stack = [(y, x)]

        while stack:
            y_, x_ = stack.pop()

            if not mask[y_, x_]:
                mask[y_, x_] = True
                size += 1
                height = heights_[y_, x_]

                if y_ > 0 and height < heights_[y_ - 1, x_] < 9:
                    stack.append((y_ - 1, x_))
                if y_ < max_y and height < heights_[y_ + 1, x_] < 9:
                    stack.append((y_ + 1, x_))
                if x_ > 0 and height < heights_[y_, x_ - 1] < 9:
                    stack.append((y_, x_ - 1))
                if x_ < max_x and height < heights_[y_, x_ + 1] < 9:
                    stack.append((y_, x_ + 1))

        insort(sizes, size)

    return sizes[-1] * sizes[-2] * sizes[-3]


if __name__ == '__main__':
    main()
