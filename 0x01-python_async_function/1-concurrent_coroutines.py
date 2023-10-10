#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random n times with the specified max_delay
    """
    delays = []

    async def call_wait_random():
        delay = await wait_random(max_delay)
        delays.append(delay)

    tasks = [call_wait_random() for _ in range(n)]
    await asyncio.gather(*tasks)
    delays.sort()
    return delays
