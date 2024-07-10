#!/usr/bin/env python3
import asyncio
import time
from typing import List
import importlib

module_name = '1-async_comprehension'
async_comprehension = importlib.import_module(module_name).async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start_time
    return total_time
