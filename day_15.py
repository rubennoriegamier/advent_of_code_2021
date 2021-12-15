import fileinput
from functools import cache, partial

import networkx as nx

OFFSETS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


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


def part_2(risk_levels: list[list[int]], scale: int = 1) -> int:
    height = len(risk_levels)
    width = len(risk_levels[0])
    scaled_height = height * scale
    scaled_width = width * scale
    graph = nx.DiGraph()

    for y, row in enumerate(risk_levels):
        for x, risk_level in enumerate(row):
            for y_scale in range(scale):
                for x_scale in range(scale):
                    scaled_y = y + height * y_scale
                    scaled_x = x + width * x_scale
                    scaled_risk_level = (risk_level - 1 + y_scale + x_scale) % 9 + 1

                    for y_offset, x_offset in OFFSETS:
                        scaled_neighbor_y = scaled_y + y_offset
                        scaled_neighbor_x = scaled_x + x_offset

                        if 0 <= scaled_neighbor_y < scaled_height and 0 <= scaled_neighbor_x < scaled_width:
                            neighbor_y_scale, neighbor_y = divmod(scaled_neighbor_y, height)
                            neighbor_x_scale, neighbor_x = divmod(scaled_neighbor_x, width)
                            neighbor_risk_level = risk_levels[neighbor_y][neighbor_x]
                            scaled_neighbor_risk_level = (neighbor_risk_level - 1
                                                          + neighbor_y_scale
                                                          + neighbor_x_scale) % 9 + 1

                            graph.add_edge((scaled_y, scaled_x), (scaled_neighbor_y, scaled_neighbor_x),
                                           weight=scaled_neighbor_risk_level)
                            graph.add_edge((scaled_neighbor_y, scaled_neighbor_x), (scaled_y, scaled_x),
                                           weight=scaled_risk_level)

    return nx.shortest_path_length(graph, (0, 0), (scaled_height - 1, scaled_width - 1), 'weight')


if __name__ == '__main__':
    main()
