from typing import Any, Iterable

from attrs import Factory, define

from quicktree.interval import Interval
from quicktree.tree import IntervalTree


@define
class NaiveTree[T: Any](IntervalTree):
    """Slow list implementation for test driving ideas"""

    intervals: list[Interval[T]] = Factory(list)
    """List of intervals"""

    def add(self, *items: Interval):
        self.intervals.extend(items)

    def at(self, time: float) -> Iterable[Interval]:
        for I in self.intervals:
            if I.A <= time < I.B:
                yield I

    def cross(self, A: float, B: float) -> Iterable[Interval]:
        for I in self.intervals:
            if (I.A <= B) and (A <= I.B):
                yield I

    def inside(self, A: float, B: float) -> Iterable[Interval]:
        for i in self.intervals:
            if (i.A >= A) and (i.B <= B):
                yield i
