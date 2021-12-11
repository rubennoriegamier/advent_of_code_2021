import fileinput
from operator import lt


def main():
    depths = list(map(int, fileinput.input()))

    print(part_1(depths))
    print(part_2(depths))


def part_1(depths: list[int]) -> int:
    return sum(map(lt, depths, depths[1:]))


def part_2(depths: list[int]) -> int:
    return sum(map(lt, depths, depths[3:]))


if __name__ == '__main__':
    main()
