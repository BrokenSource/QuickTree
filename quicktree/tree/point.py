from attrs import define

from quicktree.tree import IntervalTree


# Idea: Only query bins
@define
class PointTree(IntervalTree):
    """Optimized for point queries"""
    ...
