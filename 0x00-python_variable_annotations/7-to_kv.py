#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    create a tuple and returns 1st tuple is str & element is sq
    """
    return (k, float(v ** 2))
