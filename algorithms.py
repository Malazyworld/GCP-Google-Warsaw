"""
Sorting and Searching Algorithms Module.

This module provides implementations of fundamental algorithms, including
Binary Search and Bubble Sort, to demonstrate algorithmic logic separated
from the main application entry point.
"""

from typing import List, Optional


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sort a list of integers using the Bubble Sort algorithm.

    Bubble sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list.
    """
    n = len(arr)
    # Create a copy to avoid mutating the original input
    result = arr[:]
    
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result


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
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        else:
            high = mid - 1

    # Target was not found in the list
    return None
