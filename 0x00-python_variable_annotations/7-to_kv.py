#!/usr/bin/env python3
"""
Module for a type-annotated function to_kv that takes a string and an int or float
and returns a tuple.
"""


from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string and the square of the int/float value.

    Args:
    k (str): The string value.
    v (Union[int, float]): The int or float value to be squared.

    Returns:
    Tuple[str, float]: A tuple where the first element is the string `k` and the second element is the square of `v` as a float.
    """
    return (k, float(v ** 2))
