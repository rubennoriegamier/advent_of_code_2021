import fileinput
import re
from collections import deque

INTEGER_RE = re.compile(r'-?\d+')


def main():
    steps = list(map(Step.parse, fileinput.input()))

    print(part_1(steps))
    print(part_2(steps))


class Step:
    __slots__ = 'switch', 'x_start', 'x_stop', 'y_start', 'y_stop', 'z_start', 'z_stop'

    def __init__(self, switch, x_start, x_stop, y_start, y_stop, z_start, z_stop):
        self.switch = switch
        self.x_start = x_start
        self.x_stop = x_stop
        self.y_start = y_start
        self.y_stop = y_stop
        self.z_start = z_start
        self.z_stop = z_stop

    def __repr__(self):
        s = 'on' if self.switch else 'off'

        return f'{s} x={self.x_start}..{self.x_stop},y={self.y_start}..{self.y_stop},z={self.z_start}..{self.z_stop}'

    def __str__(self):
        return repr(self)

    def __int__(self):
        return (self.x_stop - self.x_start + 1) * (self.y_stop - self.y_start + 1) * (self.z_stop - self.z_start + 1)

    @classmethod
    def parse(cls, raw_step):
        switch, coordinates = raw_step.split()
        x_start, x_stop, y_start, y_stop, z_start, z_stop = map(int, INTEGER_RE.findall(coordinates))

        return cls(switch == 'on', x_start, x_stop, y_start, y_stop, z_start, z_stop)

    def collide(self, other):
        return (other.x_start <= self.x_stop and other.x_stop >= self.x_start and
                other.y_start <= self.y_stop and other.y_stop >= self.y_start and
                other.z_start <= self.z_stop and other.z_stop >= self.z_start)

    def split(self, other):
        if self.collide(other):
            if self.x_start < other.x_start:
                yield Step(self.switch, self.x_start, other.x_start - 1,
                           self.y_start, self.y_stop, self.z_start, self.z_stop)
            if other.x_stop < self.x_stop:
                yield Step(self.switch,
                           other.x_stop + 1, self.x_stop,
                           self.y_start, self.y_stop,
                           self.z_start, self.z_stop)

            x_start = max(self.x_start, other.x_start)
            x_stop = min(self.x_stop, other.x_stop)

            if self.y_start < other.y_start:
                yield Step(self.switch,
                           x_start, x_stop,
                           self.y_start, other.y_start - 1,
                           self.z_start, self.z_stop)
            if other.y_stop < self.y_stop:
                yield Step(self.switch,
                           x_start, x_stop,
                           other.y_stop + 1, self.y_stop,
                           self.z_start, self.z_stop)

            y_start = max(self.y_start, other.y_start)
            y_stop = min(self.y_stop, other.y_stop)

            if self.z_start < other.z_start:
                yield Step(self.switch,
                           x_start, x_stop,
                           y_start, y_stop,
                           self.z_start, other.z_start - 1)
            if other.z_stop < self.z_stop:
                yield Step(self.switch,
                           x_start, x_stop,
                           y_start, y_stop,
                           other.z_stop + 1, self.z_stop)
        else:
            yield self


def part_1(steps):
    return part_2((step for step in steps if
                   -50 <= step.z_start <= 50 and -50 <= step.z_stop <= 50 and
                   -50 <= step.y_start <= 50 and -50 <= step.y_stop <= 50 and
                   -50 <= step.x_start <= 50 and -50 <= step.x_stop <= 50))


def part_2(steps):
    steps = deque(steps)
    cubes_on = 0

    while steps:
        if steps[0].switch:
            substeps = deque()
            substeps.append(steps.popleft())

            for step in filter(substeps[0].collide, steps):
                for _ in range(len(substeps)):
                    substeps.extend(substeps.popleft().split(step))
            cubes_on += sum(map(int, substeps))
        else:
            del steps[0]

    return cubes_on


if __name__ == '__main__':
    main()
