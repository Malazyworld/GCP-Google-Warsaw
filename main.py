"""
Entry Point for the Application.

This file serves as the main entry point to showcase different features.
It adheres to the architectural guidelines of keeping logic out of main.py
and instead delegating it to feature-specific modules.
"""

from todo_app import start_todo_server
from feature_x import perform_feature_x_logic
from bubble_sort import bubble_sort
from binary_search import binary_search
from tests import run_all_tests


def example_todo_app():
    """
    Showcase the To-Do list application functionality.
    """
    print("\n--- Showcasing To-Do List Application ---")
    print("Starting the To-Do List Application server...")
    print("Open http://localhost:5001 in your browser to view the app.")
    start_todo_server()


def example_feature_x():
    """
    Showcase the functionality provided by Feature X.
    """
    print("\n--- Showcasing Feature X ---")
    result = perform_feature_x_logic("Developer")
    print(result)


def example_algorithms():
    """
    Showcase Sorting and Searching algorithms.
    """
    print("\n--- Showcasing Algorithms ---")
    
    # 1. Bubble Sort
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Unsorted List: {unsorted_list}")
    
    sorted_list = bubble_sort(unsorted_list)
    print(f"Sorted List:   {sorted_list}")
    
    # 2. Binary Search
    target = 22
    print(f"Searching for {target} in the sorted list...")
    
    index = binary_search(sorted_list, target)
    if index is not None:
        print(f"Target {target} found at index: {index}")
    else:
        print(f"Target {target} not found.")


def example_unit_tests():
    """
    Showcase the unit testing functionality.
    """
    print("\n--- Showcasing Unit Tests ---")
    success = run_all_tests()
    if success:
        print("\nAll unit tests passed successfully!")
    else:
        print("\nSome unit tests failed. Please check the output above.")


def main():
    """
    Main entry point of the script.
    
    This function coordinates the execution of example methods to showcase
    different features of the codebase.
    """
    # Showcase Feature X (non-blocking)
    example_feature_x()

    # Showcase Algorithms (non-blocking)
    example_algorithms()

    # Showcase Unit Tests (non-blocking)
    example_unit_tests()

    # Showcase the To-Do List application (blocking)
    example_todo_app()


if __name__ == '__main__':
    main()
