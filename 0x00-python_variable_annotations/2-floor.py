#!/usr/bin/env python3
"""
Module for a type-annotated function floor that takes a float
and returns the floor of the float.
"""


import math

def floor(n: float) -> int:
    """
    Returns the floor of the float number.

    Args:
    n (float): The float number to floor.

    Returns:
    int: The floor of the float number.
    """
    return math.floor(n)
