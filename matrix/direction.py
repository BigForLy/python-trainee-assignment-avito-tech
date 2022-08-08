from abc import ABC, abstractmethod
from typing import Deque, List
from .services import to_int


class AbstractDirection(ABC):
    def __init__(self, xs: List[Deque[str]], line: int) -> None:
        self.xs: List[Deque[str]] = xs
        self.line: int = line
        super().__init__()

    @abstractmethod
    def execute(self):
        raise NotImplementedError

    @abstractmethod
    def next(self):
        raise NotImplementedError


class RightDirection(AbstractDirection):
    def execute(self):
        while self.xs[self.line]:
            value = self.xs[self.line].popleft()
            yield to_int(value)
        del self.xs[self.line]

    def next(self):
        return UpDirection(self.xs, self.line)


class LeftDirection(AbstractDirection):
    def execute(self):
        while self.xs[self.line]:
            value = self.xs[self.line].pop()
            yield to_int(value)
        del self.xs[self.line]

    def next(self):
        return DownDirection(self.xs, self.line)


class UpDirection(AbstractDirection):
    def execute(self):
        for row_number in range(len(self.xs), 0, -1):
            value = self.xs[row_number - 1].pop()
            yield to_int(value)
        self.line = row_number - 1

    def next(self):
        return LeftDirection(self.xs, self.line)


class DownDirection(AbstractDirection):
    def execute(self):
        for row_number in range(len(self.xs)):
            value = self.xs[row_number].popleft()
            yield to_int(value)
        self.line = row_number

    def next(self):
        return RightDirection(self.xs, self.line)
