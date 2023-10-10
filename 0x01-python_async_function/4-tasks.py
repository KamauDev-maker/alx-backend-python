#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random n times with the specified max_delay
    """
    delays = []

    async def call_task_wait_random():
        delay = await task_wait_random(max_delay)
        delays.append(delay)

    tasks = [call_task_wait_random() for _ in range(n)]
    await asyncio.gather(*tasks)
    delays.sort()
    return delays
