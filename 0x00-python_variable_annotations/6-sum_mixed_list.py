#!/usr/bin/env python3
"""
Module for a type-annotated function sum_mixed_list that takes a list of integers and floats
and returns their sum.
"""


from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
    mxd_lst (List[Union[int, float]]): A list of integers and float numbers.

    Returns:
    float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
