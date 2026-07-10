from typing import Union

type Slice[T] = Union[T, slice[T, T, None]]
"""Either a T or slice[T, T, None] in dict[a] or dict[a:b] syntax"""

from quicktree.interval import Interval
from quicktree.tree.naive import NaiveTree
