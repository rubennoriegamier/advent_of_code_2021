import fileinput
from collections import defaultdict, deque
from collections.abc import Iterable
from itertools import takewhile
from operator import methodcaller

Connections = defaultdict[str, list[str]]


def main():
    connections: Connections = parse_connections(map(str.rstrip, fileinput.input()))

    print(part_1(connections))
    print(part_2(connections))


def parse_connections(raw_connections: Iterable[str]) -> Connections:
    connections = defaultdict(list)

    for a, b in map(methodcaller('split', '-'), raw_connections):
        if a != 'end' and b != 'start':
            connections[a].append(b)
        if a != 'start' and b != 'end':
            connections[b].append(a)

    return connections


def part_1(connections: Connections) -> int:
    visited = set()

    def move(curr_cave):
        if curr_cave == 'end':
            return 1

        paths = 0

        if curr_cave.islower():
            visited.add(curr_cave)
        for next_cave in connections[curr_cave]:
            if next_cave.isupper() or next_cave not in visited:
                paths += move(next_cave)
        if curr_cave.islower():
            visited.remove(curr_cave)

        return paths

    return sum(map(move, connections['start']))


def part_2(connections: Connections) -> int:
    visited = deque()

    def move(curr_cave: str, double_visit: bool = False) -> int:
        if curr_cave == 'end':
            return 1

        paths = 0

        visited.appendleft(curr_cave)
        for next_cave in connections[curr_cave]:
            if next_cave.isupper():
                if all(map(next_cave.__ne__, takewhile(str.isupper, visited))):
                    paths += move(next_cave, double_visit=double_visit)
            elif next_cave not in visited:
                paths += move(next_cave, double_visit=double_visit)
            elif not double_visit:
                paths += move(next_cave, double_visit=True)
        del visited[0]

        return paths

    return sum(map(move, connections['start']))


if __name__ == '__main__':
    main()
