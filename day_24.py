import fileinput
from functools import cache

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
    instruction_groups = list(split_at(instructions, lambda instruction: instruction[0] == 'inp'))[1:]
    match part:
        case 1:
            range_ = range(9, 0, -1)
        case 2:
            range_ = range(1, 10)
        case _:
            raise NotImplementedError()

    @cache
    def solve(idx, w, x, y, z):
        for instruction in instruction_groups[idx]:
            match instruction[0]:
                case 'add':
                    match instruction[1]:
                        case 'x':
                            match instruction[2]:
                                case 'w':
                                    x += w
                                case 'y':
                                    x += y
                                case 'z':
                                    x += z
                                case _:
                                    x += instruction[2]
                        case 'y':
                            match instruction[2]:
                                case 'w':
                                    y += w
                                case 'x':
                                    y += x
                                case 'z':
                                    y += z
                                case _:
                                    y += instruction[2]
                        case 'z':
                            match instruction[2]:
                                case 'w':
                                    z += w
                                case 'x':
                                    z += x
                                case 'y':
                                    z += y
                                case _:
                                    z += instruction[2]
                case 'mul':
                    match instruction[1]:
                        case 'x':
                            match instruction[2]:
                                case 'w':
                                    x *= w
                                case 'y':
                                    x *= y
                                case 'z':
                                    x *= z
                                case _:
                                    x *= instruction[2]
                        case 'y':
                            match instruction[2]:
                                case 'w':
                                    y *= w
                                case 'x':
                                    y *= x
                                case 'z':
                                    y *= z
                                case _:
                                    y *= instruction[2]
                        case 'z':
                            match instruction[2]:
                                case 'w':
                                    z *= w
                                case 'x':
                                    z *= x
                                case 'y':
                                    z *= y
                                case _:
                                    z *= instruction[2]
                case 'div':
                    match instruction[1]:
                        case 'x':
                            match instruction[2]:
                                case 'w':
                                    x //= w
                                case 'y':
                                    x //= y
                                case 'z':
                                    x //= z
                                case _:
                                    x //= instruction[2]
                        case 'y':
                            match instruction[2]:
                                case 'w':
                                    y //= w
                                case 'x':
                                    y //= x
                                case 'z':
                                    y //= z
                                case _:
                                    y //= instruction[2]
                        case 'z':
                            match instruction[2]:
                                case 'w':
                                    z //= w
                                case 'x':
                                    z //= x
                                case 'y':
                                    z //= y
                                case _:
                                    z //= instruction[2]
                case 'mod':
                    match instruction[1]:
                        case 'x':
                            match instruction[2]:
                                case 'w':
                                    x %= w
                                case 'y':
                                    x %= y
                                case 'z':
                                    x %= z
                                case _:
                                    x %= instruction[2]
                        case 'y':
                            match instruction[2]:
                                case 'w':
                                    y %= w
                                case 'x':
                                    y %= x
                                case 'z':
                                    y %= z
                                case _:
                                    y %= instruction[2]
                        case 'z':
                            match instruction[2]:
                                case 'w':
                                    z %= w
                                case 'x':
                                    z %= x
                                case 'y':
                                    z %= y
                                case _:
                                    z %= instruction[2]
                case 'eql':
                    match instruction[1]:
                        case 'x':
                            match instruction[2]:
                                case 'w':
                                    x = int(x == w)
                                case 'y':
                                    x = int(x == y)
                                case 'z':
                                    x = int(x == z)
                                case _:
                                    x = int(x == instruction[2])
                        case 'y':
                            match instruction[2]:
                                case 'w':
                                    y = int(y == w)
                                case 'x':
                                    y = int(y == x)
                                case 'z':
                                    y = int(y == z)
                                case _:
                                    y = int(y == instruction[2])
                        case 'z':
                            match instruction[2]:
                                case 'w':
                                    z = int(z == w)
                                case 'x':
                                    z = int(z == x)
                                case 'y':
                                    z = int(z == y)
                                case _:
                                    z = int(z == instruction[2])

        if idx == 13:
            if z == 0:
                return w
        else:
            for digit_ in range_:
                result_ = solve(idx + 1, digit_, x, y, z)
                if result_:
                    return f'{w}{result_}'

    for digit in range_:
        result = solve(0, digit, 0, 0, 0)
        if result:
            return int(result)


if __name__ == '__main__':
    main()
