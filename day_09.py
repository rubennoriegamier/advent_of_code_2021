import fileinput
from bisect import insort
from functools import partial

import numpy as np
# noinspection PyProtectedMember
from numpy.lib.stride_tricks import as_strided


def main():
    heights: list[list[int]] = list(map(list, map(partial(map, int), map(str.rstrip, fileinput.input()))))

    print(part_1(heights))
    print(part_2(heights))


def part_1(heights: list[list[int]]) -> int:
    height = len(heights)
    width = len(heights[0])
    height_with_pad = height + 2
    width_with_pad = width + 2

    heights_ = np.full((height_with_pad, width_with_pad), 127, np.byte)
    heights_[1:-1, 1:-1] = heights

    lower_adjacent = as_strided(heights_.flat[1:], (height, width, 2, 2),
                                (width_with_pad, 1, width_with_pad + 1, width_with_pad - 1)) \
        .min((2, 3), initial=127).reshape((height, -1))
    mask = np.less(heights_[1:-1, 1:-1], lower_adjacent)

    return (heights_[1:-1, 1:-1][mask] + 1).sum()


def part_2(heights: list[list[int]]) -> int:
    height = len(heights)
    width = len(heights[0])
    height_with_pad = height + 2
    width_with_pad = width + 2

    heights_ = np.full((height_with_pad, width_with_pad), 127, np.byte)
    heights_[1:-1, 1:-1] = heights

    lower_adjacent = as_strided(heights_.flat[1:], (height, width, 2, 2),
                                (width_with_pad, 1, width_with_pad + 1, width_with_pad - 1)) \
        .min((2, 3), initial=127).reshape((height, -1))
    mask = np.less(heights_[1:-1, 1:-1], lower_adjacent)
    indexes = np.transpose(np.nonzero(mask))
    indexes += 1

    def go_up(y_: int, x_: int) -> int:
        if heights_[y_, x_] < heights_[y_ - 1, x_] < 9 and not mask[y_ - 2, x_ - 1]:
            mask[y_ - 2, x_ - 1] = True
            return 1 + go_up(y_ - 1, x_) + go_left(y_ - 1, x_) + go_right(y_ - 1, x_)
        return 0

    def go_down(y_: int, x_: int) -> int:
        if heights_[y_, x_] < heights_[y_ + 1, x_] < 9 and not mask[y_, x_ - 1]:
            mask[y_, x_ - 1] = True
            return 1 + go_down(y_ + 1, x_) + go_left(y_ + 1, x_) + go_right(y_ + 1, x_)
        return 0

    def go_left(y_: int, x_: int) -> int:
        if heights_[y_, x_] < heights_[y_, x_ - 1] < 9 and not mask[y_ - 1, x_ - 2]:
            mask[y_ - 1, x_ - 2] = True
            return 1 + go_up(y_, x_ - 1) + go_down(y_, x_ - 1) + go_left(y_, x_ - 1)
        return 0

    def go_right(y_: int, x_: int) -> int:
        if heights_[y_, x_] < heights_[y_, x_ + 1] < 9 and not mask[y_ - 1, x_]:
            mask[y_ - 1, x_] = True
            return 1 + go_up(y_, x_ + 1) + go_down(y_, x_ + 1) + go_right(y_, x_ + 1)
        return 0

    sizes = []

    for y, x in indexes:
        insort(sizes, 1 + go_up(y, x) + go_down(y, x) + go_left(y, x) + go_right(y, x))

    return sizes[-1] * sizes[-2] * sizes[-3]


if __name__ == '__main__':
    main()
