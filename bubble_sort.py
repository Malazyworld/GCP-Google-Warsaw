"""
Bubble Sort Algorithm Module.
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sort a list of integers using the Bubble Sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list.
    """
    n = len(arr)
    result = arr[:]
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result
