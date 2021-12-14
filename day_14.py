from collections import Counter
from functools import cache, partial, reduce
from itertools import pairwise
from operator import add, methodcaller
from sys import stdin


def main():
    template, raw_insertion_rules = stdin.read().rstrip().split('\n\n')
    insertion_rules = parse_insertion_rules(raw_insertion_rules)

    print(part_1(template, insertion_rules))
    print(part_2(template, insertion_rules))


def parse_insertion_rules(raw_insertion_rules: str) -> dict[str, str]:
    return {key: f'{key[0]}{value}{key[1]}'
            for key, value in map(methodcaller('split', ' -> '), raw_insertion_rules.split('\n'))}


def most_common_minus_least_common(template: str, insertion_rules: dict[str, str], steps: int) -> int:
    @cache
    def get_counter(template_: str, steps_: int) -> Counter:
        if steps_ == 0:
            return Counter(template_)

        return reduce(add, map(partial(get_counter, steps_=steps_ - 1),
                               map(insertion_rules.get, map(''.join, pairwise(template_))))) - Counter(template_[1:-1])

    most_common = get_counter(template, steps).most_common()

    return most_common[0][1] - most_common[-1][1]


def part_1(template: str, insertion_rules: dict[str, str]) -> int:
    return most_common_minus_least_common(template, insertion_rules, 10)


def part_2(template: str, insertion_rules: dict[str, str]) -> int:
    return most_common_minus_least_common(template, insertion_rules, 40)


if __name__ == '__main__':
    main()
