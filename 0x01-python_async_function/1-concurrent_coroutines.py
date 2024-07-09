#!/usr/bin/env python3
"""
This module provides an asynchronous routine that spawns multiple wait_random coroutines.
"""

import asyncio
from typing import List
import importlib

# Dynamically import the module with a hyphen in its name
module_name = '0-basic_async_syntax'
wait_random = importlib.import_module(module_name).wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.
    
    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random coroutine.
    
    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
