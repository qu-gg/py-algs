"""
@file mergesort.py
@author qu-gg

Implementation of a MergeSort algorithm
"""


def merge_sort(array):
    """
    Implementation of mergesort, which recursively breaks down a list into two halves until they are
    length 1 arrays and then builds them up the stack
    :param array: array to break apart
    :return: sorted array at that stage
    """
    length = len(array)
    sorted = []
    if length < 2:
        return array
    else:
        # Calculating midpoint and splitting arrays
        mid_point = length // 2         
        first_half = array[:mid_point]
        second_half = array[mid_point:]

        # Sorting the split arrays
        first_half = merge_sort(first_half)          
        second_half = merge_sort(second_half)

        # Sorting the arrays based on comparison
        f = s = 0
        while f < len(first_half) and s < len(second_half):     
            if first_half[f] < second_half[s]:
                sorted.append(first_half[f])
                f += 1
            else:
                sorted.append(second_half[s])
                s += 1

        # Checking if any elements remain in the arrays
        while f < len(first_half):      
            sorted.append(first_half[f])
            f += 1

        while s < len(second_half):
            sorted.append(second_half[s])
            s += 1

    return sorted
