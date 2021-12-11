import fileinput
from functools import partial
from itertools import count

import numpy as np


def main():
    energy_levels: list[list[int]] = list(map(list, map(partial(map, int), map(str.rstrip, fileinput.input()))))

    print(part_1(energy_levels))
    print(part_2(energy_levels))


def part_1(energy_levels: list[list[int]]) -> int:
    energy_levels_ = np.asarray(energy_levels, np.byte)
    flashes_mask = np.empty_like(energy_levels_, bool)
    aux_mask = np.empty_like(energy_levels_, bool)
    flashes_count = 0

    for _ in range(100):
        energy_levels_ += 1

        flashes_mask[:] = False
        np.equal(energy_levels_, 10, out=aux_mask)

        while aux_mask.any():
            energy_levels_[1:, 1:][aux_mask[:-1, :-1]] += 1
            energy_levels_[1:][aux_mask[:-1]] += 1
            energy_levels_[1:, :-1][aux_mask[:-1, 1:]] += 1
            energy_levels_[:, 1:][aux_mask[:, :-1]] += 1
            energy_levels_[:, :-1][aux_mask[:, 1:]] += 1
            energy_levels_[:-1, 1:][aux_mask[1:, :-1]] += 1
            energy_levels_[:-1][aux_mask[1:]] += 1
            energy_levels_[:-1, :-1][aux_mask[1:, 1:]] += 1

            np.logical_or(flashes_mask, aux_mask, out=flashes_mask)
            np.logical_not(flashes_mask, out=aux_mask)
            np.greater_equal(energy_levels_, 10, out=aux_mask, where=aux_mask)

        energy_levels_[flashes_mask] = 0
        flashes_count += np.count_nonzero(flashes_mask)

    return flashes_count


def part_2(energy_levels: list[list[int]]) -> int:
    energy_levels_ = np.asarray(energy_levels, np.byte)
    flashes_mask = np.empty_like(energy_levels_, bool)
    aux_mask = np.empty_like(energy_levels_, bool)

    for n in count(1):
        energy_levels_ += 1

        flashes_mask[:] = False
        np.equal(energy_levels_, 10, out=aux_mask)

        while aux_mask.any():
            energy_levels_[1:, 1:][aux_mask[:-1, :-1]] += 1
            energy_levels_[1:][aux_mask[:-1]] += 1
            energy_levels_[1:, :-1][aux_mask[:-1, 1:]] += 1
            energy_levels_[:, 1:][aux_mask[:, :-1]] += 1
            energy_levels_[:, :-1][aux_mask[:, 1:]] += 1
            energy_levels_[:-1, 1:][aux_mask[1:, :-1]] += 1
            energy_levels_[:-1][aux_mask[1:]] += 1
            energy_levels_[:-1, :-1][aux_mask[1:, 1:]] += 1

            np.logical_or(flashes_mask, aux_mask, out=flashes_mask)
            np.logical_not(flashes_mask, out=aux_mask)
            np.greater_equal(energy_levels_, 10, out=aux_mask, where=aux_mask)

        energy_levels_[flashes_mask] = 0

        if np.count_nonzero(flashes_mask) == energy_levels_.size:
            return n


if __name__ == '__main__':
    main()
