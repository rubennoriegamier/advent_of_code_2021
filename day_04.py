from collections import defaultdict
from collections.abc import Iterable
from functools import reduce
from os import linesep
from sys import stdin


def main():
    numbers = list(map(int, input().split(',')))
    boards = list(map(parse_board, stdin.read().lstrip().split(linesep * 2)))

    print(part_1(numbers, boards))
    print(part_2(numbers, boards))


def parse_board(raw_board: str) -> list[list[int]]:
    return list(list(map(int, line.split())) for line in raw_board.split(linesep))


class BoardGame:
    _size: int
    _positions: dict[int, tuple[int, int]]
    _crossed_by_row: defaultdict[int, set]
    _crossed_by_col: defaultdict[int, set]
    _last_crossed: int | None

    def __init__(self, board: list[list[int]]):
        self._size = len(board)
        self._positions = {board_number: (row_idx, col_idx)
                           for row_idx, row in enumerate(board)
                           for col_idx, board_number in enumerate(row)}
        self._crossed_by_row = defaultdict(set)
        self._crossed_by_col = defaultdict(set)
        self._last_crossed = None

    def cross(self, number: int) -> bool:
        if self._last_crossed is None:
            position = self._positions.get(number)

            if position is not None:
                row_crossed = self._crossed_by_row[position[0]]
                col_crossed = self._crossed_by_col[position[1]]

                row_crossed.add(number)
                col_crossed.add(number)
                if len(row_crossed) == self._size or len(col_crossed) == self._size:
                    self._last_crossed = number

                    return True

        return False

    @property
    def score(self) -> int | None:
        if self._last_crossed is not None:
            # noinspection PyUnresolvedReferences
            marked_numbers_sum = sum(reduce(set.union, self._crossed_by_row.values())
                                     | reduce(set.union, self._crossed_by_col.values()))

            return (sum(self._positions.keys()) - marked_numbers_sum) * self._last_crossed


def part_1(numbers: Iterable[int], boards: Iterable[list[list[int]]]) -> int | None:
    board_games = list(map(BoardGame, boards))

    for number in numbers:
        for board_game in board_games:
            if board_game.cross(number):
                return board_game.score


def part_2(numbers: Iterable[int], boards: Iterable[list[list[int]]]) -> int | None:
    board_games = list(map(BoardGame, boards))
    last_to_win: BoardGame | None = None

    for number in numbers:
        i = 0

        while i < len(board_games):
            if board_games[i].cross(number):
                last_to_win = board_games[i]

                del board_games[i]
            else:
                i += 1

    return last_to_win.score if last_to_win else None


if __name__ == '__main__':
    main()
