from collections import Counter
from functools import cache
from itertools import cycle, product


def main():
    p_1_pos = int(input().rsplit(maxsplit=1)[1])
    p_2_pos = int(input().rsplit(maxsplit=1)[1])

    print(part_1(p_1_pos, p_2_pos))
    print(part_2(p_1_pos, p_2_pos))


def part_1(p_1_pos, p_2_pos):
    p_1_pos -= 1
    p_2_pos -= 1
    dice = cycle(range(1, 101))
    p_1_pts = 0
    p_2_pts = 0
    rolled = 0

    while True:
        p_1_pos += next(dice) + next(dice) + next(dice)
        rolled += 3
        p_1_pos %= 10
        p_1_pts += p_1_pos + 1
        if p_1_pts >= 1_000:
            return p_2_pts * rolled
        p_2_pos += next(dice) + next(dice) + next(dice)
        rolled += 3
        p_2_pos %= 10
        p_2_pts += p_2_pos + 1
        if p_2_pts >= 1_000:
            return p_1_pts * rolled


def part_2(p_1_pos, p_2_pos):
    p_1_pos -= 1
    p_2_pos -= 1
    dice_combinations_sum = Counter(map(sum, product([1, 2, 3], repeat=3)))

    @cache
    def solve(p_1_pos_, p_2_pos_, p_1_pts, p_2_pts):
        p_1_wins = 0
        p_2_wins = 0

        for p_1_dice_combination_sum, p_1_dice_combination_times in dice_combinations_sum.items():
            p_1_pos__ = (p_1_pos_ + p_1_dice_combination_sum) % 10
            p_1_pts_ = p_1_pts + p_1_pos__ + 1

            if p_1_pts_ >= 21:
                p_1_wins += p_1_dice_combination_times
            else:
                for p_2_dice_combination_sum, p_2_dice_combination_times in dice_combinations_sum.items():
                    p_2_pos__ = (p_2_pos_ + p_2_dice_combination_sum) % 10
                    p_2_pts_ = p_2_pts + p_2_pos__ + 1

                    if p_2_pts_ >= 21:
                        p_2_wins += p_1_dice_combination_times * p_2_dice_combination_times
                    else:
                        p_1_wins_, p_2_wins_ = solve(p_1_pos__, p_2_pos__, p_1_pts_, p_2_pts_)
                        p_1_wins += p_1_wins_ * p_1_dice_combination_times * p_2_dice_combination_times
                        p_2_wins += p_2_wins_ * p_1_dice_combination_times * p_2_dice_combination_times

        return p_1_wins, p_2_wins

    return max(*solve(p_1_pos, p_2_pos, 0, 0))


if __name__ == '__main__':
    main()
