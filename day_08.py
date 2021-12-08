import fileinput
from collections import Counter
from collections.abc import Iterable
from itertools import chain, groupby
from operator import itemgetter

CHARS = 'abcdefg'
DIGITS = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4',
          'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}
FIRST_ITEM_GETTER = itemgetter(0)
SECOND_ITEM_GETTER = itemgetter(1)

Entry = tuple[tuple[str, str, str, str, str, str, str, str, str, str], tuple[str, str, str, str]]


def main():
    entries = list(map(parse_entry, fileinput.input()))

    print(part_1(entries))
    print(part_2(entries))


def parse_entry(raw_entry: str) -> Entry:
    # noinspection PyTypeChecker
    return tuple(map(tuple, map(str.split, raw_entry.split(' | '))))


def part_1(entries: Iterable[Entry]) -> int:
    counts = Counter(map(len, chain.from_iterable(map(SECOND_ITEM_GETTER, entries))))

    return counts.get(1, 0) + counts.get(4, 0) + counts.get(7, 0) + counts.get(8, 0) << 1


def decode_entry(entry: Entry) -> int:
    candidates = {}
    pattern_signals = sorted(entry[0], key=len)

    # 1
    candidates[pattern_signals[0][0]] = {'c', 'f'}
    candidates[pattern_signals[0][1]] = {'c', 'f'}
    for char in CHARS:
        if char not in pattern_signals[0]:
            candidates[char] = {'a', 'b', 'd', 'e', 'g'}

    # 7
    for idx in range(3):
        candidates[pattern_signals[1][idx]].difference_update('bdeg')
    for char in CHARS:
        if char not in pattern_signals[1]:
            candidates[char].difference_update('acf')

    # 4
    for idx in range(4):
        candidates[pattern_signals[2][idx]].difference_update('aeg')
    for char in CHARS:
        if char not in pattern_signals[2]:
            candidates[char].difference_update('bcdf')

    # 2, 3, and 5
    counter = Counter(chain.from_iterable(pattern_signals[3:6]))

    for char, times in counter.items():
        match times:
            case 1:
                candidates[char].difference_update('acdfg')
            case 2:
                candidates[char].difference_update('abdeg')
            case 3:
                candidates[char].difference_update('bcef')
    for times, chars in groupby(counter.most_common(), key=SECOND_ITEM_GETTER):
        chars = ''.join(map(FIRST_ITEM_GETTER, chars))

        for char in CHARS:
            if char not in chars:
                match times:
                    case 1:
                        candidates[char].difference_update('be')
                    case 2:
                        candidates[char].difference_update('cf')
                    case 3:
                        candidates[char].difference_update('adg')

    # 0, 6, and 9
    counter = Counter(chain.from_iterable(pattern_signals[6:9]))

    for char, times in counter.items():
        match times:
            case 2:
                candidates[char].difference_update('abfg')
            case 3:
                candidates[char].difference_update('cde')
    for times, chars in groupby(counter.most_common(), key=SECOND_ITEM_GETTER):
        chars = ''.join(map(FIRST_ITEM_GETTER, chars))

        for char in CHARS:
            if char not in chars:
                match times:
                    case 2:
                        candidates[char].difference_update('cde')
                    case 3:
                        candidates[char].difference_update('abfg')

    trans = str.maketrans(*map(''.join, zip(*((char, chars.pop()) for char, chars in candidates.items()))))

    return int(''.join(DIGITS[''.join(sorted(encoded_digit.translate(trans)))] for encoded_digit in entry[1]))


def part_2(entries: Iterable[Entry]) -> int:
    return sum(map(decode_entry, entries))


if __name__ == '__main__':
    main()
