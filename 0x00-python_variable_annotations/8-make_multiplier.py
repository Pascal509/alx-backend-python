#!/usr/bin/env python3
"""
Module for a type-annotated function make_multiplier that takes a float multiplier and
returns a function that multiplies a float by the multiplier.
"""


from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    Args:
    multiplier (float): The multiplier value.

    Returns:
    Callable[[float], float]: A function that takes a float and returns it multiplied by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    
    return multiplier_function
