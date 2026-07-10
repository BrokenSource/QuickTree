from typing import Any

from attrs import define


@define(frozen=True, eq=False)
class Interval[T: Any]:

    data: T
    """Interval data"""

    A: float
    """Interval start"""

    B: float
    """Interval end"""

    def __hash__(self) -> int:
        return id(self.data)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Interval):
            raise TypeError
        return self.data is other.data
