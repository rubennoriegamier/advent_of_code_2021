import fileinput
from collections import Counter
from collections.abc import Iterable, Iterator
from functools import partial
from itertools import tee
from operator import itemgetter


def main():
    bin_numbers = list(map(str.rstrip, fileinput.input()))

    print(part_1(bin_numbers))
    print(part_2(bin_numbers))


def part_1(bin_numbers: Iterable[str]) -> int:
    bin_gamma_rate = ''.join(Counter(bits).most_common(1)[0][0] for bits in zip(*bin_numbers))

    return int(bin_gamma_rate, 2) * int(bin_gamma_rate.translate(str.maketrans('01', '10')), 2)


def part_2(bin_numbers: Iterable[str]) -> int:
    ab: list[Iterator[str]]
    *ab, c = tee(bin_numbers, 3)

    def string_idx_eq_to(idx: int, char: str, string: str) -> bool:
        return string[idx] == char

    try:
        # 0 for the first column of bits
        # 1 for the second column of bits
        # ...
        for i in range(len(next(c))):
            # 0 for oxygen generator rating
            # 1 for CO2 scrubber rating
            for j in range(2):
                ab[j], ab_for_most_common = tee(ab[j])
                most_common: list[tuple[str, int]] = Counter(map(itemgetter(i), ab_for_most_common)).most_common()

                if len(most_common) == 2:
                    # str(0 ^ 1) == '1', the default value for the oxygen generator rating when there is a tie
                    # str(1 ^ 1) == '0', the default value for the CO2 scrubber rating when there is a tie
                    ab[j] = filter(partial(string_idx_eq_to, i,
                                           str(j ^ 1) if most_common[0][1] == most_common[1][1] else most_common[j][0]),
                                   ab[j])
    except StopIteration:
        return 0

    return int(next(ab[0]), 2) * int(next(ab[1]), 2)


if __name__ == '__main__':
    main()
