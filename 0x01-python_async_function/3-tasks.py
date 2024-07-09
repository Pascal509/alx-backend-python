#!/usr/bin/env python3
"""
This module provides a function to create an asyncio.Task from wait_random coroutine.
"""

import asyncio
import importlib

module_name = '0-basic_async_syntax'
wait_random = importlib.import_module(module_name).wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random coroutine with the given max_delay.
    
    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.
    
    Returns:
        asyncio.Task: The created asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
