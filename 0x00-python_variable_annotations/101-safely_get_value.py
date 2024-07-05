#!/usr/bin/env python3
"""
Module for a type-annotated function safely_get_value that retrieves a value from a dictionary safely.
"""


from typing import Mapping, Any, Union, TypeVar

# Define a type variable ~T
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Retrieves a value from a dictionary safely.

    Args:
    dct (Mapping): A mapping (like a dictionary) where the value needs to be retrieved.
    key (Any): The key whose value needs to be retrieved from the dictionary.
    default (Union[T, None], optional): The default value to return if the key is not present in the dictionary.
    Defaults to None.

    Returns:
    Union[Any, T]: The value associated with the key in the dictionary if present, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

if __name__ == "__main__":
    # Example usage
    my_dict = {'a': 1, 'b': 2}
    print(safely_get_value(my_dict, 'a'))  # Output: 1
    print(safely_get_value(my_dict, 'c', 'Not found'))  # Output: 'Not found'
