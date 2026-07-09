from abc import ABC, abstractmethod
from typing import Any

from attrs import define

# ---------------------------------------------------------------------------- #

@define(frozen=True, eq=False)
class Interval:

    data: Any
    """Interval data"""

    a: float
    """Interval start"""

    b: float
    """Interval end"""

    def __hash__(self) -> int:
        return id(self.data)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Interval):
            return False
        return self.data is other.data

# ---------------------------------------------------------------------------- #

@define
class _IntervalTree(ABC):
    """Trait that all interval trees must implement"""

    @abstractmethod
    def at(self, point: float) -> list[Interval]:
        ...

    @abstractmethod
    def add(self, interval: Interval) -> None:
        ...

# ---------------------------------------------------------------------------- #

@define
class QuickTree(_IntervalTree):

    intervals: list[Interval]
    """List of intervals"""

    granularity: int = 1
    """Bin size for intervals"""

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
