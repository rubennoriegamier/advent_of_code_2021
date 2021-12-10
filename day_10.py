import fileinput
from bisect import insort


def main():
    lines: list[str] = list(map(str.rstrip, fileinput.input()))

    print(part_1(lines))
    print(part_2(lines))


def part_1(lines: list[str]) -> int:
    points = 0

    for line in lines:
        chars = []

        for char in line:
            match char:
                case ')':
                    if chars[-1] == '(':
                        del chars[-1]
                    else:
                        points += 3
                        break
                case ']':
                    if chars[-1] == '[':
                        del chars[-1]
                    else:
                        points += 57
                        break
                case '}':
                    if chars[-1] == '{':
                        del chars[-1]
                    else:
                        points += 1_197
                        break
                case '>':
                    if chars[-1] == '<':
                        del chars[-1]
                    else:
                        points += 25_137
                        break
                case _:
                    chars.append(char)

    return points


def part_2(lines: list[str]) -> int:
    scores = []

    for line in lines:
        chars = []

        for char in line:
            match char:
                case ')':
                    if chars[-1] == '(':
                        del chars[-1]
                    else:
                        break
                case ']':
                    if chars[-1] == '[':
                        del chars[-1]
                    else:
                        break
                case '}':
                    if chars[-1] == '{':
                        del chars[-1]
                    else:
                        break
                case '>':
                    if chars[-1] == '<':
                        del chars[-1]
                    else:
                        break
                case _:
                    chars.append(char)
        else:
            score = 0

            for char in chars[::-1]:
                match char:
                    case '(':
                        score = score * 5 + 1
                    case '[':
                        score = score * 5 + 2
                    case '{':
                        score = score * 5 + 3
                    case '<':
                        score = score * 5 + 4

            insort(scores, score)

    return scores[len(scores) >> 1]


if __name__ == '__main__':
    main()
