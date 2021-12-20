import re
from itertools import islice


def main():
    x_start, x_end, y_start, y_end = map(int, re.findall('(-?\\d+)', input()))

    print(part_1(y_start))
    print(part_2(x_start, x_end, y_start, y_end))


def part_1(y_start: int) -> int:
    return y_start * y_start + y_start >> 1


def part_2(x_start: int, x_end: int, y_start: int, y_end: int) -> int:
    vel_values = 0

    for y_vel in range(y_start, abs(y_start)):
        y_pos = 0

        if y_vel >= 0:
            steps = y_vel << 1 | 1
            y_vel_ = -y_vel - 1
        else:
            steps = 0
            y_vel_ = y_vel

        while y_pos > y_end:
            steps += 1
            y_pos += y_vel_
            y_vel_ -= 1

        for x_vel in range(x_end, -1, -1):
            x_pos = sum(islice(range(x_vel, 0, -1), steps))
            x_vel = max(x_vel - steps, 0)

            if x_pos < x_start and x_vel == 0:
                break

            y_pos_ = y_pos
            y_vel__ = y_vel_

            while y_pos_ >= y_start and x_pos <= x_end:
                if y_pos_ <= y_end and x_pos >= x_start:
                    vel_values += 1
                    break

                y_pos_ += y_vel__
                y_vel__ -= 1
                x_pos += x_vel
                x_vel = max(x_vel - 1, 0)

    return vel_values


if __name__ == '__main__':
    main()
