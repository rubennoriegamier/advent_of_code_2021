import re
from functools import cache
from itertools import chain, groupby
from operator import itemgetter
from sys import stdin

import networkx as nx


def main():
    aa, bb, cc, dd = parse_positions(stdin.read())

    print(part_1(aa, bb, cc, dd))
    print(part_2(aa, bb, cc, dd))


def parse_positions(diagram):
    for _, nn in groupby(sorted(zip(re.findall('[ABCD]', diagram),
                                    [(1, 2), (1, 4), (1, 6), (1, 8), (2, 2), (2, 4), (2, 6), (2, 8)])), itemgetter(0)):
        yield tuple(map(itemgetter(1), nn))


#              0
#    01234567891
#   #############
# 0 #...........#
# 1 ###.#.#.#.###
# 2   #.#.#.#.#
#     #########
def part_1(aa, bb, cc, dd):
    hallway_xs = 0, 1, 3, 5, 7, 9, 10
    graph = nx.Graph()
    shortest_path = cache(lambda source, target: nx.shortest_path(graph, source, target)[1:])

    for x in range(10):
        graph.add_edge((0, x), (0, x + 1))
    for x in (2, 4, 6, 8):
        for y in range(len(aa)):
            graph.add_edge((y, x), (y + 1, x))

    @cache
    def solve(aa_, bb_, cc_, dd_):
        if (all(a[1] == 2 for a in aa_) and
                all(b[1] == 4 for b in bb_) and
                all(c[1] == 6 for c in cc_) and
                all(d[1] == 8 for d in dd_)):
            return 0

        energy = float('inf')
        occupied = set(chain(aa_, bb_, cc_, dd_))

        for nn_idx, nn in enumerate((aa_, bb_, cc_, dd_)):
            args = [aa_, bb_, cc_, dd_]
            room_x = nn_idx + 1 << 1
            weight = 10 ** nn_idx

            for n_idx, n in enumerate(nn):
                if n[0] > 0:
                    if n[1] != room_x or sum(1 for n_ in nn[n_idx + 1:] if n_[1] == room_x) < len(nn) - n[0]:
                        for hallway_x in hallway_xs:
                            path = shortest_path(n, (0, hallway_x))
                            if not any(map(occupied.__contains__, path)):
                                args[nn_idx] = tuple(sorted(chain(nn[:n_idx], path[-1:], nn[n_idx + 1:])))
                                energy = min(energy, len(path) * weight + solve(*args))
                else:
                    # noinspection PyShadowingNames
                    for y in range(len(nn), 0, -1):
                        if (y, room_x) in occupied:
                            if (y, room_x) not in nn:
                                break
                        else:
                            path = shortest_path(n, (y, room_x))
                            if not any(map(occupied.__contains__, path)):
                                args[nn_idx] = tuple(sorted(chain(nn[:n_idx], path[-1:], nn[n_idx + 1:])))
                                energy = min(energy, len(path) * weight + solve(*args))
                            break

        return energy

    return solve(tuple(sorted(aa)), tuple(sorted(bb)), tuple(sorted(cc)), tuple(sorted(dd)))


def part_2(aa, bb, cc, dd):
    aa = sorted(aa)
    bb = sorted(bb)
    cc = sorted(cc)
    dd = sorted(dd)

    for nn in (aa, bb, cc, dd):
        for idx in range(len(nn)):
            if nn[idx][0] == 2:
                nn[idx] = 4, nn[idx][1]

    aa = tuple(chain(aa, ((3, 6), (2, 8))))
    bb = tuple(chain(bb, ((3, 4), (2, 6))))
    cc = tuple(chain(cc, ((2, 4), (3, 8))))
    dd = tuple(chain(dd, ((2, 2), (3, 2))))

    return part_1(aa, bb, cc, dd)


if __name__ == '__main__':
    main()
