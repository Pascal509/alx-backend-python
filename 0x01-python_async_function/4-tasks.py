#!/usr/bin/env python3
"""
This module provides an asynchronous routine that spawns multiple task_wait_random coroutines.
"""

import asyncio
from typing import List
import importlib

module_name = '3-tasks'
task_wait_random = importlib.import_module(module_name).task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n times with the specified max_delay.
    
    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay for each task_wait_random coroutine.
    
    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
