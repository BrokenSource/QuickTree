from typing import Union

__about__   = "🌲 Fast interval trees for python"
__package__ = "quicktree"
__version__ = "0.1.0"
__license__ = "MIT"

type Slice[T] = Union[T, slice[T, T, None]]
"""Either a T or slice[T, T, None] for dict[a] or dict[a:b] syntax"""

from quicktree.interval import Interval
from quicktree.tree.naive import NaiveTree
