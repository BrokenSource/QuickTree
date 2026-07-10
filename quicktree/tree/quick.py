from attrs import define

from quicktree.tree import IntervalTree


# Idea: Use best methods in Point, Overlap, Between at the
# cost of slower insertion and memory
@define
class QuickTree(IntervalTree):
    """Optimized for point queries"""
    ...
