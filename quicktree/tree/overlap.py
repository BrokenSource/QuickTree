from attrs import define

from quicktree.tree import IntervalTree


# Idea: Faith on granularity
@define
class OverlapTree(IntervalTree):
    ...
