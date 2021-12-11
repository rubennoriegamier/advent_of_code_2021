import fileinput
from functools import partial
from itertools import count


def main():
    energy_levels: list[list[int]] = list(map(list, map(partial(map, int), map(str.rstrip, fileinput.input()))))

    print(part_1(energy_levels))
    print(part_2(energy_levels))


# noinspection PyTypeChecker
def part_1(energies: list[list[int]]) -> int:
    max_y = len(energies) - 1
    max_x = len(energies[0]) - 1
    energies = list(map(list.copy, energies))
    flashes = 0

    for _ in range(100):
        stack = []

        for y, row in enumerate(energies):
            for x in range(len(row)):
                if row[x] == 9:
                    stack.append((y, x))
                else:
                    row[x] += 1

        while stack:
            y, x = stack.pop()

            if energies[y][x] > 0:
                energies[y][x] += 1
                if energies[y][x] == 10:
                    flashes += 1
                    energies[y][x] = 0

                    if y == 0:
                        stack.append((y + 1, x))
                        if x == 0:
                            stack.append((y, x + 1))
                            stack.append((y + 1, x + 1))
                        elif x == max_x:
                            stack.append((y, x - 1))
                            stack.append((y + 1, x - 1))
                        else:
                            stack.append((y, x - 1))
                            stack.append((y, x + 1))
                            stack.append((y + 1, x - 1))
                            stack.append((y + 1, x + 1))
                    elif y == max_y:
                        stack.append((y - 1, x))
                        if x == 0:
                            stack.append((y - 1, x + 1))
                            stack.append((y, x + 1))
                        elif x == max_x:
                            stack.append((y - 1, x - 1))
                            stack.append((y, x - 1))
                        else:
                            stack.append((y - 1, x - 1))
                            stack.append((y - 1, x + 1))
                            stack.append((y, x - 1))
                            stack.append((y, x + 1))
                    else:
                        stack.append((y - 1, x))
                        stack.append((y + 1, x))
                        if x == 0:
                            stack.append((y - 1, x + 1))
                            stack.append((y, x + 1))
                            stack.append((y + 1, x + 1))
                        elif x == max_x:
                            stack.append((y - 1, x - 1))
                            stack.append((y, x - 1))
                            stack.append((y + 1, x - 1))
                        else:
                            stack.append((y - 1, x - 1))
                            stack.append((y - 1, x + 1))
                            stack.append((y, x - 1))
                            stack.append((y, x + 1))
                            stack.append((y + 1, x - 1))
                            stack.append((y + 1, x + 1))

    return flashes


# noinspection PyTypeChecker
def part_2(energies: list[list[int]]) -> int:
    max_y = len(energies) - 1
    max_x = len(energies[0]) - 1
    size = len(energies) * len(energies[0])
    energies = list(map(list.copy, energies))

    for n in count(1):
        flashes = 0
        stack = []

        for y, row in enumerate(energies):
            for x in range(len(row)):
                if row[x] == 9:
                    stack.append((y, x))
                else:
                    row[x] += 1

        while stack:
            y, x = stack.pop()

            if energies[y][x] > 0:
                energies[y][x] += 1
                if energies[y][x] == 10:
                    flashes += 1
                    energies[y][x] = 0

                    if y == 0:
                        stack.append((y + 1, x))
                        if x == 0:
                            stack.append((y, x + 1))
                            stack.append((y + 1, x + 1))
                        elif x == max_x:
                            stack.append((y, x - 1))
                            stack.append((y + 1, x - 1))
                        else:
                            stack.append((y, x - 1))
                            stack.append((y, x + 1))
                            stack.append((y + 1, x - 1))
                            stack.append((y + 1, x + 1))
                    elif y == max_y:
                        stack.append((y - 1, x))
                        if x == 0:
                            stack.append((y - 1, x + 1))
                            stack.append((y, x + 1))
                        elif x == max_x:
                            stack.append((y - 1, x - 1))
                            stack.append((y, x - 1))
                        else:
                            stack.append((y - 1, x - 1))
                            stack.append((y - 1, x + 1))
                            stack.append((y, x - 1))
                            stack.append((y, x + 1))
                    else:
                        stack.append((y - 1, x))
                        stack.append((y + 1, x))
                        if x == 0:
                            stack.append((y - 1, x + 1))
                            stack.append((y, x + 1))
                            stack.append((y + 1, x + 1))
                        elif x == max_x:
                            stack.append((y - 1, x - 1))
                            stack.append((y, x - 1))
                            stack.append((y + 1, x - 1))
                        else:
                            stack.append((y - 1, x - 1))
                            stack.append((y - 1, x + 1))
                            stack.append((y, x - 1))
                            stack.append((y, x + 1))
                            stack.append((y + 1, x - 1))
                            stack.append((y + 1, x + 1))

        if flashes == size:
            return n


if __name__ == '__main__':
    main()
