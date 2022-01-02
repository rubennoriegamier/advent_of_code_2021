import fileinput
from functools import cache, partial
from operator import itemgetter

from more_itertools import split_at


def main():
    instructions = list(map(parse_instruction, map(str.rstrip, fileinput.input())))

    print(part_1_and_2(instructions, 1))
    print(part_1_and_2(instructions, 2))


def parse_instruction(raw_instruction):
    instruction, *placeholders = raw_instruction.split()

    if len(placeholders) == 1:
        return instruction, placeholders[0]
    if placeholders[1] in 'wxyz':
        return instruction, placeholders[0], placeholders[1]
    return instruction, placeholders[0], int(placeholders[1])


def part_1_and_2(instructions, part):
    operands = list(map(list, map(partial(map, itemgetter(2)),
                                  split_at(instructions, lambda instruction: instruction[0] == 'inp'))))[1:]
    match part:
        case 1:
            range_ = range(9, 0, -1)
        case 2:
            range_ = range(1, 10)
        case _:
            raise NotImplementedError()

    @cache
    def solve(idx, w, z):
        # noinspection PyTypeChecker
        if z % 26 + operands[idx][4] == w:
            z //= operands[idx][3]
        else:
            z = z // operands[idx][3] * 26 + (w + operands[idx][14])

        if idx == 13:
            if z == 0:
                return w
        else:
            for digit_ in range_:
                partial_solution = solve(idx + 1, digit_, z)

                if partial_solution:
                    return f'{w}{partial_solution}'

    return int(next(filter(None, (solve(0, digit, 0) for digit in range_))))


if __name__ == '__main__':
    main()
