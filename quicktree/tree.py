from abc import ABC, abstractmethod
from typing import Any, Iterable, Union

from attrs import Factory, define

from quicktree.interval import Interval


@define
class IntervalTree[T: Any](ABC):
    """Trait that all interval trees must implement"""

    @abstractmethod
    def at(self, time: float) -> Iterable[Interval[T]]:
        ...

    @abstractmethod
    def add(self, /, interval: Interval[T]) -> None:
        ...

    @abstractmethod
    def overlap(self, A: float, B: float) -> Iterable[Interval[T]]:
        ...

    def __getitem__(self,
        time: Union[float, slice[float]]
    ) -> Iterable[Interval[T]]:

        # Syntax: tree[a:b]
        if isinstance(time, slice):
            yield from self.overlap(
                A=time.start,
                B=time.stop,
            )

        # Syntax: tree[a]
        else:
            yield from self.at(time)

    def __setitem__(self,
        time: Union[float, slice[float]],
        data: T
    ) -> None:
        # Syntax: tree[a:b]
        if isinstance(time, slice):
            self.add(Interval(
                A=time.start,
                B=time.stop,
                data=data,
            ))

        else:
            # Syntax: tree[a]
            self.add(Interval(
                A=time,B=time,
                data=data,
            ))

# ---------------------------------------------------------------------------- #

@define
class QuickTree[T: Any](IntervalTree):

    intervals: list[Interval[T]] = Factory(list)
    """List of intervals"""

    granularity: float = 1
    """Bin size for intervals"""

    def at(self, time: float) -> Iterable[Interval]:
        for I in self.intervals:
            if I.A <= time < I.B:
                yield I

    def add(self, /, interval: Interval) -> None:
        self.intervals.append(interval)

    def overlap(self, A: float, B: float) -> Iterable[Interval]:
        for I in self.intervals:
            if I.B <= A or B <= I.A:
                yield I

# ---------------------------------------------------------------------------- #

# Idea: Only query bins
@define
class PointTree(IntervalTree):
    """Optimized for point queries"""
    ...

# Idea: Only keep track of interval starts (free dedupe)
@define
class BetweenTree(IntervalTree):
    """Optimized for range queries"""
    ...

# Idea: Faith on granularity
@define
class OverlapTree(IntervalTree):
    ...
