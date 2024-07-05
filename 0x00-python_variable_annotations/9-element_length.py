#!/usr/bin/env python3
"""
Module for a type-annotated function element_length that takes an iterable and returns a list of tuples.
"""


from typing import Iterable, Sequence, Tuple, List

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element from the input list and its length.

    Args:
    lst (Iterable[Sequence]): An iterable of sequences (like lists or strings).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where the first element of each tuple is an element from lst and the second element is its length.
    """
    return [(i, len(i)) for i in lst]
