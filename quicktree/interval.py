from attrs import define


@define(frozen=True, eq=False)
class Interval[T]:

    A: float
    """Interval start"""

    B: float
    """Interval end"""

    data: T
    """Interval data"""

    def is_point(self) -> bool:
        """Whether start equals ending"""
        return (self.A == self.B)

    def __hash__(self) -> int:
        return id(self.data)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Interval):
            raise TypeError
        return self.data is other.data
