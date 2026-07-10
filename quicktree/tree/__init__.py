from abc import ABC, abstractmethod
from typing import Any, Iterable

from attrs import define

from quicktree import Slice
from quicktree.interval import Interval


@define
class IntervalTree[T](ABC):
    """Trait that all interval trees must implement"""

    @abstractmethod
    def add(self, *items: Interval[T]) -> None:
        """Add an interval to the tree"""

    @abstractmethod
    def at(self, /, time: float) -> Iterable[Interval[T]]:
        """Get all active intervals at this point"""

    @abstractmethod
    def cross(self, /, A: float, B: float) -> Iterable[Interval[T]]:
        """Get all active intervals touching the range"""

    @abstractmethod
    def inside(self, /, A: float, B: float) -> Iterable[Interval[T]]:
        """Get all active intervals inside the range"""

    # # Dict-like setters and getters

    def __getitem__(self, time: Slice[float]) -> Iterable[Interval[T]]:
        """
        Syntax dependent:
        - `tree[t]`:   yields self.at(t)
        - `tree[a:b]`: yields self.cross(a, b)
        """

        # Syntax: tree[a:b]
        if isinstance(time, slice):
            yield from self.cross(
                A=time.start,
                B=time.stop,
            )

        # Syntax: tree[a]
        else:
            yield from self.at(time)

    def __setitem__(self, time: Slice[float], data: T) -> None:

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
