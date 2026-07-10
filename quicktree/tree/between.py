from attrs import define

from quicktree.tree import IntervalTree


# Idea: Only keep track of interval starts (free dedupe)
@define
class BetweenTree(IntervalTree):
    """Optimized for range queries"""
    ...
