#!/usr/bin/env python3
"""
Coroutine called async_comprehension that takes no args
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collects async generated list and return it
    """
    random_numbers = [num async for num in async_generator()]
    return random_numbers
