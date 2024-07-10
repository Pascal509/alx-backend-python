#!/usr/bin/env python3
from typing import List
import importlib

module_name = '0-async_generator'
async_generator = importlib.import_module(module_name).async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [number async for number in async_generator()]
