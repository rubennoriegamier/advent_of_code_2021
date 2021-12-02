import fileinput
from collections.abc import Iterable


def main():
    commands: list[str] = list(fileinput.input())

    print(part_1(commands))
    print(part_2(commands))


def part_1(commands: Iterable[str]) -> int:
    horizontal_position = 0
    depth = 0

    command: str
    units: str

    for command, units in map(str.split, commands):
        units: int = int(units)

        match command:
            case 'forward':
                horizontal_position += units
            case 'down':
                depth += units
            case 'up':
                depth -= units

    return depth * horizontal_position


def part_2(commands: Iterable[str]) -> int:
    horizontal_position = 0
    depth = 0
    aim = 0

    command: str
    units: str

    for command, units in map(str.split, commands):
        units: int = int(units)

        match command:
            case 'forward':
                horizontal_position += units
                depth += aim * units
            case 'down':
                aim += units
            case 'up':
                aim -= units

    return depth * horizontal_position


if __name__ == '__main__':
    main()
