"""
Binary Search Algorithm Module.
"""

from typing import List, Optional


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Search for a target value within a sorted list using Binary Search.

    Args:
        arr (List[int]): A sorted list of integers to search in.
        target (int): The value to search for.

    Returns:
        Optional[int]: The index of the target if found, otherwise None.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None
