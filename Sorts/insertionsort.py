"""
@file insertionsory.py
@author qu-gg

Implementatin of the InsertionSort algorithm
"""

def insertion_sort(array):
    """
    Implementation of Insertion Sort, which puts each element of an array into its correct place before
    continuing the iteration
    :param array: array to sort
    :return: sorted array
    """
    counter = 1
    
    while counter < len(array):
        index = counter
        while index > 0 and array[index - 1] > array[index]:
            temp = array[index]
            array[index] = array[index - 1]
            array[index - 1] = temp
            index -= 1
        counter += 1
    
    return array
