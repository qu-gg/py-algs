"""
@file bucketsort.py
@author qu-gg

Implementation of BucketSort using InsertionSort underneath
"""


def insertion_sort(array):
    """
    Implementation of Insertion Sort, which puts each element of an array into its correct place before
    continuing the iteration
    :param array: array to sort
    :return:
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


def bucket_sort(array, radix):
    """
    Implementation of Bucket Sort, which splits up values into different buckets and sorts those buckets
    individually before concatenating them in order
    :param array: array to sort
    :param radix: number of buckets
    :return: sorted array
    """
    buckets = [[] for _ in range(radix)]
    for num in array:
        buckets[int(num * radix)].append(num)

    for bucket in buckets:
        if len(bucket) > 1:
            insertion_sort(bucket)

    sorted = []
    for bucket in buckets:
        sorted += bucket

    return sorted
