from collections import deque
from collections.abc import Generator, Iterable
from enum import Enum, auto
from functools import partial
from itertools import combinations
from sys import stdin


def main():
    scanners: list[Scanner] = list(map(Scanner.parse, stdin.read().rstrip().split('\n\n')))

    print(*part_1_and_2(scanners), sep='\n')


class AxisRotation(Enum):
    X_Clockwise = auto()
    X_Counterclockwise = auto()
    Y_Clockwise = auto()
    Y_Counterclockwise = auto()
    Z_Clockwise = auto()
    Z_Counterclockwise = auto()


class Scanner:
    _ROTATIONS = [AxisRotation.Y_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.Z_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.X_Counterclockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.X_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.X_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.Z_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.Y_Clockwise,
                  AxisRotation.Y_Clockwise]

    beacons: set[tuple[int, int, int]]

    def __init__(self, coordinates: Iterable[tuple[int, int, int]]):
        self.beacons = set(coordinates)

    def __add__(self, other: 'Scanner') -> tuple['Scanner', tuple[int, int, int]]:
        for orientation in other.orientations():
            for x_a, y_a, z_a in self.beacons:
                for x_b, y_b, z_b in orientation.beacons:
                    x_scanner = x_a - x_b
                    y_scanner = y_a - y_b
                    z_scanner = z_a - z_b
                    if sum(1 for x_c, y_c, z_c in orientation.beacons
                           if (x_c + x_scanner, y_c + y_scanner, z_c + z_scanner) in self.beacons) >= 12:
                        return Scanner(self.beacons | {(x_c + x_scanner, y_c + y_scanner, z_c + z_scanner)
                                                       for x_c, y_c, z_c in orientation.beacons}), (x_scanner,
                                                                                                    y_scanner,
                                                                                                    z_scanner)

    def rotate(self, axis: AxisRotation) -> None:
        match axis:
            case AxisRotation.X_Clockwise:
                self.beacons = {(x, -z, y) for x, y, z in self.beacons}
            case AxisRotation.X_Counterclockwise:
                self.beacons = {(x, z, -y) for x, y, z in self.beacons}
            case AxisRotation.Y_Clockwise:
                self.beacons = {(-z, y, x) for x, y, z in self.beacons}
            case AxisRotation.Y_Counterclockwise:
                self.beacons = {(z, y, -x) for x, y, z in self.beacons}
            case AxisRotation.Z_Clockwise:
                self.beacons = {(y, -x, z) for x, y, z in self.beacons}
            case AxisRotation.Z_Counterclockwise:
                self.beacons = {(-y, x, z) for x, y, z in self.beacons}

    def orientations(self) -> Generator['Scanner']:
        yield self
        for axis_rotation in self._ROTATIONS:
            self.rotate(axis_rotation)
            yield self

    @classmethod
    def parse(cls, raw_coordinates) -> 'Scanner':
        return cls(map(tuple, map(partial(map, int), map(partial(str.split, sep=','),
                                                         raw_coordinates.split('\n')[1:]))))


def part_1_and_2(scanners: list[Scanner]) -> tuple[int, int]:
    scanners = deque(scanners)
    full_map = scanners.popleft()
    scanners_coordinates = [(0, 0, 0)]

    while scanners:
        scanner = scanners.popleft()
        new_full_map_and_scanner_coordinates = full_map + scanner
        if new_full_map_and_scanner_coordinates:
            full_map = new_full_map_and_scanner_coordinates[0]
            scanners_coordinates.append(new_full_map_and_scanner_coordinates[1])
        else:
            scanners.append(scanner)

    return len(full_map.beacons), max(abs(x_a - x_b) + abs(y_a - y_b) + abs(z_a - z_b)
                                      for (x_a, y_a, z_a), (x_b, y_b, z_b) in combinations(scanners_coordinates, 2))


if __name__ == '__main__':
    main()
