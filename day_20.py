import fileinput
from functools import partial
from operator import eq

import numpy as np
# noinspection PyProtectedMember
from numpy.lib.stride_tricks import as_strided

IS_LIGHT = partial(eq, '#')


def main():
    algorithm = parse_algorithm(input())
    print(algorithm)
    input()
    image = parse_image(map(str.rstrip, fileinput.input()))

    print(part_1_and_2(algorithm, image, 2))
    print(part_1_and_2(algorithm, image, 50))


def parse_algorithm(raw_algorithm):
    return np.fromiter(map(IS_LIGHT, raw_algorithm), np.int16, len(raw_algorithm))


def parse_image(raw_image):
    return list(map(list, map(partial(map, IS_LIGHT), raw_image)))


def part_1_and_2(algorithm, image, times):
    bit_mask = np.asarray([[256, 128, 64], [32, 16, 8], [4, 2, 1]], np.int16)
    image = np.asarray(image, np.int16)

    for time_ in range(times):
        image = np.pad(image, 2, constant_values=1 if time_ % 2 == 1 and algorithm[0] == 1 else 0)
        squares = as_strided(image, (image.shape[0] - 2, image.shape[1] - 2, 3, 3), image.strides * 2, writeable=False)
        image = (squares * bit_mask).sum((2, 3), np.int16)
        algorithm.take(image, out=image)

    return image.sum()


if __name__ == '__main__':
    main()
