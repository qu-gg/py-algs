"""
@file minheap.py
@author qu-gg

Basic implementation of a MinHeap using an Array
"""


class MinHeap:
    def __init__(self):
        # Init for the heap list
        self.heap = list()

    def parent(self, index):
        # Function to get the parent index of an object
        return (index - 1) // 2

    def left_child(self, index):
        # Function to get the left child index of an object
        return (index * 2) + 1

    def right_child(self, index):
        # Function to get the right child index of an object
        return (index * 2) + 2

    def insert(self, node):
        """
        Handles the insertion of a node into the tree
        :param node: node to add
        """
        if len(self.heap) == 0:
            self.heap.append(node)
            return

        self.heap.append(node)
        self.sift_up(len(self.heap) - 1)
    
    def sift_up(self, index):
        """
        Handles sifting a node up in the heap after insertion
        :param index: index of the node to sift
        """
        par = self.parent(index)

        if index > 0 and self.heap[index] < self.heap[par]:
            temp = self.heap[index]
            self.heap[index] = self.heap[par]
            self.heap[par] = temp
            self.sift_up(par)

    def remove(self):
        """
        Handles removing the root node from the heap
        :return: value of the root node if it exists
        """
        if len(self.heap) == 0:
            return
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            value = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.sift_down(0)
            return value

    def sift_down(self, index):
        """
        Handles sifting a node down the tree
        :param: index of the node to sift down
        """
        left = self.left_child(index)
        right = self.right_child(index)

        if right < len(self.heap) and self.heap[right] < self.heap[left]:
            maximum = right
        else:
            maximum = left

        if maximum < len(self.heap) and self.heap[maximum] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[maximum]
            self.heap[maximum] = temp
            self.sift_down(maximum)
