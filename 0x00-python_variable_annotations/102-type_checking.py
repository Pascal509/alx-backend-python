#!/usr/bin/env python3
"""
Module for a type-annotated function zoom_array that zooms into a tuple array.
"""


from typing import Tuple, List, Any

def zoom_array(lst: Tuple[Any,...], factor: int = 2) -> Tuple[Any,...]:
    """
    Zooms into a tuple array by repeating each element by a given factor.

    Args:
    lst (Tuple[Any]): The tuple array to be zoomed into.
    factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
    Tuple[Any]: The zoomed-in tuple array.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)

if __name__ == "__main__":
    # Example usage
    array = (12, 72, 91)

    zoom_2x = zoom_array(array)
    print(zoom_2x)

    zoom_3x = zoom_array(array, 3)  # Corrected to use integer 3 instead of float 3.0
    print(zoom_3x)
