from functools import cache


def main():
    timers = list(map(int, input().split(',')))

    print(part_1(timers))
    print(part_2(timers))


@cache
def descendants(days: int) -> int:
    return sum(1 + descendants(day - 9) for day in range(days, -1, -7))


def part_1(timers: list[int]) -> int:
    return sum(1 + descendants(80 - timer - 1) for timer in timers)


def part_2(timers: list[int]) -> int:
    return sum(1 + descendants(256 - timer - 1) for timer in timers)


if __name__ == '__main__':
    main()
