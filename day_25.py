import fileinput
from functools import partial
from itertools import count

import numpy as np

CHAR_MAP = {'.': 0, '>': 1, 'v': 2}


def main():
    seafloor_map = parse_seafloor_map(map(str.rstrip, fileinput.input()))

    print(part_1(seafloor_map))


def parse_seafloor_map(raw_seafloor_map):
    return np.asarray(list(map(list, map(partial(map, CHAR_MAP.get), raw_seafloor_map))), np.byte)


def part_1(seafloor_map):
    east_mask = np.empty_like(seafloor_map, bool)
    south_mask = np.empty_like(seafloor_map, bool)

    for step in count(1):
        # East
        np.equal(seafloor_map, 0, out=east_mask)
        np.equal(seafloor_map[:, :-1], 1, out=east_mask[:, 1:], where=east_mask[:, 1:])
        np.equal(seafloor_map[:, -1], 1, out=east_mask[:, 0], where=east_mask[:, 0])
        seafloor_map[:, :-1][east_mask[:, 1:]] = 0
        seafloor_map[:, -1][east_mask[:, 0]] = 0
        seafloor_map[east_mask] = 1

        # South
        np.equal(seafloor_map, 0, out=south_mask)
        np.equal(seafloor_map[:-1], 2, out=south_mask[1:], where=south_mask[1:])
        np.equal(seafloor_map[-1], 2, out=south_mask[0], where=south_mask[0])
        seafloor_map[:-1][south_mask[1:]] = 0
        seafloor_map[-1][south_mask[0]] = 0
        seafloor_map[south_mask] = 2

        if not east_mask.any() and not south_mask.any():
            return step


if __name__ == '__main__':
    main()
