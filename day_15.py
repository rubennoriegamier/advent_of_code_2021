import fileinput
from functools import cache, partial

import networkx as nx
import numpy as np
# noinspection PyProtectedMember
from numpy.lib.stride_tricks import as_strided


def main():
    risk_levels: list[list[int]] = list(map(list, map(partial(map, int), map(str.rstrip, fileinput.input()))))

    print(part_1(risk_levels))
    print(part_2(risk_levels, 5))


def part_1(risk_levels: list[list[int]]) -> int:
    height = len(risk_levels)
    width = len(risk_levels[0])

    @cache
    def solve(y: int, x: int) -> int | float:
        if y < height and x < width:
            risk_level = risk_levels[y][x]

            if y == height - 1 and x == width - 1:
                return risk_level

            return risk_level + min(solve(y + 1, x), solve(y, x + 1))

        return float('inf')

    return min(solve(1, 0), solve(0, 1))


def part_2(risk_levels: list[list[int]], scale: int) -> int:
    risk_levels = np.asarray(risk_levels, dtype=np.byte)
    height, width = risk_levels.shape
    scaled_height = height * scale
    scaled_width = width * scale
    scaled_risk_levels = np.zeros((scaled_height + 2, scaled_width + 2), np.byte)
    scaled_risk_levels[1:-1, 1:-1] = as_strided(np.arange(-1, scale - 1 << 1, dtype=np.byte),
                                                (scale, height, scale, width), (1, 0, 1, 0)) \
        .reshape((scaled_height, -1))

    for y in range(0, scaled_height, height):
        for x in range(0, scaled_width, width):
            scaled_risk_levels[y + 1:y + height + 1, x + 1:x + width + 1] += risk_levels
    scaled_risk_levels %= 9
    scaled_risk_levels += 1

    graph = nx.DiGraph()

    for y in range(1, scaled_height + 1):
        for x in range(1, scaled_width + 1):
            yx = y, x

            graph.add_edge(yx, (y - 1, x), weight=scaled_risk_levels[y - 1, x])
            graph.add_edge(yx, (y + 1, x), weight=scaled_risk_levels[y + 1, x])
            graph.add_edge(yx, (y, x - 1), weight=scaled_risk_levels[y, x - 1])
            graph.add_edge(yx, (y, x + 1), weight=scaled_risk_levels[y, x + 1])

    return nx.shortest_path_length(graph, (1, 1), (scaled_height, scaled_width), 'weight')


if __name__ == '__main__':
    main()
