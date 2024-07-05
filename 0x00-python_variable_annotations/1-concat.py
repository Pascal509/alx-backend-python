#!/usr/bin/env python3
"""
Module for a type-annotated function concat that takes two strings
and returns their concatenated result.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Args:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    str: The concatenated string of str1 and str2.
    """
    return str1 + str2
