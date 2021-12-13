from functools import partial
from operator import itemgetter, methodcaller
from sys import stdin

Dot = tuple[int, int]
Fold = tuple[str, int]


def main():
    raw_dots, raw_folds = stdin.read().rstrip().split('\n\n')
    dots = parse_dots(raw_dots)
    folds = parse_folds(raw_folds)

    print(part_1(dots, folds))
    part_2(dots, folds)


def parse_dots(raw_dots: str) -> list[Dot]:
    return list(map(tuple, map(partial(map, int), map(methodcaller('split', ','), raw_dots.split('\n')))))


def parse_folds(raw_folds: str) -> list[Fold]:
    return [(coordinate, int(value)) for coordinate, value in
            map(methodcaller('split', '='), map(itemgetter(2), map(str.split, raw_folds.split('\n'))))]


def print_dots(dots):
    width = 0
    height = 0

    for x, y in dots:
        width = max(width, x + 1)
        height = max(height, y + 1)

    grid = [list(' ' * width) for _ in range(height)]

    for x, y in dots:
        grid[y][x] = '#'

    print(*map(''.join, grid), sep='\n')


def part_1(dots: list[Dot], folds: list[Fold], part_1_=True) -> int:
    dots = set(dots)

    for coordinate, value in folds:
        new_dots = set()

        if coordinate == 'x':
            for x, y in dots:
                if x < value:
                    new_dots.add((x, y))
                else:
                    new_dots.add((value * 2 - x, y))
        else:
            for x, y in dots:
                if y < value:
                    new_dots.add((x, y))
                else:
                    new_dots.add((x, value * 2 - y))

        dots = new_dots

        if part_1_:
            return len(dots)

    print_dots(dots)


def part_2(dots: list[Dot], folds: list[Fold]) -> None:
    part_1(dots, folds, part_1_=False)


if __name__ == '__main__':
    main()
