from abc import ABC, abstractmethod
from typing import Any, Iterable, Union

from attrs import Factory, define

type Time = float

# ---------------------------------------------------------------------------- #

@define(frozen=True, eq=False)
class Interval[T: Any]:

    data: T
    """Interval data"""

    A: Time
    """Interval start"""

    B: Time
    """Interval end"""

    def __hash__(self) -> int:
        return id(self.data)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Interval):
            raise TypeError
        return self.data is other.data

# ---------------------------------------------------------------------------- #

@define
class _IntervalTree[T: Any](ABC):
    """Trait that all interval trees must implement"""

    @abstractmethod
    def at(self, time: Time) -> Iterable[Interval[T]]:
        ...

    @abstractmethod
    def add(self, /, interval: Interval[T]) -> None:
        ...

    @abstractmethod
    def overlap(self, A: Time, B: Time) -> Iterable[Interval[T]]:
        ...

    def __getitem__(self,
        time: Union[Time, slice[Time]]
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
        time: Union[Time, slice[Time]],
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
class QuickTree[T: Any](_IntervalTree):

    intervals: list[Interval[T]] = Factory(list)
    """List of intervals"""

    granularity: Time = 1
    """Bin size for intervals"""

    def at(self, time: Time) -> Iterable[Interval]:
        for I in self.intervals:
            if I.A <= time < I.B:
                yield I

    def add(self, /, interval: Interval) -> None:
        self.intervals.append(interval)

    def overlap(self, A: Time, B: Time) -> Iterable[Interval]:
        for I in self.intervals:
            if I.B <= A or B <= I.A:
                yield I

# ---------------------------------------------------------------------------- #

# Idea: Only query bins
@define
class PointTree(_IntervalTree):
    """Optimized for point queries"""
    ...

# Idea: Only keep track of interval starts (free dedupe)
@define
class BetweenTree(_IntervalTree):
    """Optimized for range queries"""
    ...

# Idea: Faith on granularity
@define
class OverlapTree(_IntervalTree):
    ...
