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
    mask = np.empty_like(seafloor_map, bool)

    for step in count(1):
        # East
        np.equal(seafloor_map, 0, out=mask)
        np.equal(seafloor_map[:, :-1], 1, out=mask[:, 1:], where=mask[:, 1:])
        np.equal(seafloor_map[:, -1], 1, out=mask[:, 0], where=mask[:, 0])
        seafloor_map[:, :-1][mask[:, 1:]] = 0
        seafloor_map[:, -1][mask[:, 0]] = 0
        seafloor_map[mask] = 1

        any_ = mask.any()

        # South
        np.equal(seafloor_map, 0, out=mask)
        np.equal(seafloor_map[:-1], 2, out=mask[1:], where=mask[1:])
        np.equal(seafloor_map[-1], 2, out=mask[0], where=mask[0])
        seafloor_map[:-1][mask[1:]] = 0
        seafloor_map[-1][mask[0]] = 0
        seafloor_map[mask] = 2

        if not any_ and not mask.any():
            return step


if __name__ == '__main__':
    main()
