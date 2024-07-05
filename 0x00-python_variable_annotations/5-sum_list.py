#!/usr/bin/env python3
"""
Module for a type-annotated function sum_list that takes a list of floats
and returns their sum.
"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
    input_list (List[float]): A list of float numbers.

    Returns:
    float: The sum of the float numbers in the list.
    """
    return sum(input_list)
