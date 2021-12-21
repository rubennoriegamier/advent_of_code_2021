import fileinput
import re
from collections import Counter
from functools import reduce
from itertools import permutations

PAIR_RE = re.compile(r'\[\d+,\d+]')
INT_RE = re.compile(r'\d+')
GE_10_RE = re.compile(r'\d{2,}')


def main():
    snailfish_numbers: list[str] = list(map(str.rstrip, fileinput.input()))

    print(part_1(snailfish_numbers))
    print(part_2(snailfish_numbers))


def split(n: str) -> str:
    n = int(n)

    return f'[{n >> 1},{n + 1 >> 1}]'


def reduce_snailfish_number(snailfish_number: str) -> str:
    while True:
        for match in PAIR_RE.finditer(snailfish_number):
            start_idx, end_idx = match.span()
            counter = Counter(snailfish_number[:start_idx])
            if counter['['] - counter[']'] >= 4:
                n_1, n_2 = map(int, match.group()[1:-1].split(','))
                prefix = INT_RE.sub(lambda m: str(int(m.group()[::-1]) + n_1)[::-1],
                                    snailfish_number[start_idx - 1::-1], 1)[::-1]
                suffix = INT_RE.sub(lambda m: str(int(m.group()) + n_2),
                                    snailfish_number[end_idx:], 1)
                snailfish_number = f'{prefix}0{suffix}'
                break
        else:
            snailfish_number, subs = GE_10_RE.subn(lambda m: split(m.group()), snailfish_number, 1)
            if subs == 0:
                return snailfish_number


def pair_magnitude(pair: str) -> int:
    n_1, n_2 = map(int, pair[1:-1].split(','))

    return n_1 * 3 + n_2 * 2


def magnitude(snailfish_number: str) -> int:
    while snailfish_number[0] == '[':
        snailfish_number = PAIR_RE.sub(lambda m: str(pair_magnitude(m.group())), snailfish_number)

    return int(snailfish_number)


def part_1(snailfish_numbers: list[str]) -> int:
    return magnitude(reduce(lambda acc, sn: reduce_snailfish_number(f'[{acc},{sn}]'), snailfish_numbers))


def part_2(snailfish_numbers: list[str]) -> int:
    return max(magnitude(reduce_snailfish_number(f'[{sn_1},{sn_2}]'))
               for sn_1, sn_2 in permutations(snailfish_numbers, 2))


if __name__ == '__main__':
    main()
