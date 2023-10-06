#!/usr/bin/env python3
"""
Type an iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of the elements
    """
    return [(i, len(i)) for i in lst]
