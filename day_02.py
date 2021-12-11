import fileinput


def main():
    commands: list[Command] = list(map(Command.parse, fileinput.input()))

    print(part_1(commands))
    print(part_2(commands))


class Command:
    __slots__ = 'command', 'units'

    command: str
    units: int

    def __init__(self, command, units):
        self.command = command
        self.units = units

    @classmethod
    def parse(cls, raw_command: str) -> 'Command':
        command, raw_units = raw_command.split()

        return cls(command, int(raw_units))


def part_1(commands: list[Command]) -> int:
    horizontal_position = 0
    depth = 0

    for command in commands:
        match command.command:
            case 'forward':
                horizontal_position += command.units
            case 'down':
                depth += command.units
            case 'up':
                depth -= command.units

    return depth * horizontal_position


def part_2(commands: list[Command]) -> int:
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in commands:
        match command.command:
            case 'forward':
                horizontal_position += command.units
                depth += aim * command.units
            case 'down':
                aim += command.units
            case 'up':
                aim -= command.units

    return depth * horizontal_position


if __name__ == '__main__':
    main()
