from enum import Enum, auto
from typing import List
from collections import deque
from memory_profiler import profile


class Direction(Enum):
    up = auto()
    down = auto()
    left = auto()
    rigth = auto()


class Algorithm:
    def __init__(self, xs) -> None:
        self.xs: List[deque[str]] = xs
        self.direction = Direction.down
        self.line = 0
        self.result: List[int] = []

    def start(self) -> List[int]:
        while self.xs:
            self.next()
        return self.result

    @profile
    def next(self):
        match self.direction:
            case Direction.up:
                for row_number in range(len(self.xs), 0, -1):
                    value = self.xs[row_number-1].pop()
                    self.result.append(to_int(value))
                    self.line = row_number-1
                self.direction = Direction.left
            case Direction.down:
                for row_number in range(len(self.xs)):
                    value = self.xs[row_number].popleft()
                    self.result.append(to_int(value))
                    self.line = row_number
                self.direction = Direction.rigth
            case Direction.left:
                while self.xs[self.line]:
                    value = self.xs[self.line].pop()
                    self.result.append(to_int(value))
                del self.xs[self.line]
                self.direction = Direction.down
            case Direction.rigth:
                while self.xs[self.line]:
                    value = self.xs[self.line].popleft()
                    self.result.append(to_int(value))
                del self.xs[self.line]
                self.direction = Direction.up


def to_int(value: str | int) -> int:
    return value if isinstance(value, int) else int(value)
