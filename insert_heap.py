"""Author - Anantvir Singh, concept reference:= Data Structures in C by Seymour Lipschutz"""

# This shows array implementation of heap. Linked list representation requires significantly more effort as contruction of
# complete binary tree requires maintaining a queue and heap insertion operations need continuous manipulation of that queue
 
import math
class MaxHeap:
    class Node:
        def __init__(self,item,parent =None,left_child = None,right_child = None):
            self._item = item
            self._parent = parent                   # Parent, left and right not required in this implementation, although more information about the node can be included in place of them
            self._left_child = left_child
            self._right_child = right_child
    
    def __init__(self):
        self.TREE = []


    def insert_heap(self,item):
        newNode = self.Node(item)
        self.TREE.append(newNode)
        ptr = self.TREE.index(newNode)      # Get index of last element inserted which will act as pointer to current node

        while ptr > 0:
            par = math.floor(ptr/2)         # Calculate parent
            if newNode._item < self.TREE[par]._item:    # New item less than parent ?
                self.TREE[ptr] = newNode                # then Insert new item at current pointer position
                return newNode
            self.TREE[ptr] = self.TREE[par]             # New Item greater than parent ? then move down parent to current pointer and update current pointer
            ptr = par                                   # Current pointer = parent --> Move up the pointer
        if ptr == 0:                                    # If pointer becomes root
            self.TREE[ptr] = newNode
        return newNode

h = MaxHeap()
h.insert_heap(4)
h.insert_heap(9)
h.insert_heap(66)
h.insert_heap(50)
h.insert_heap(76)
h.insert_heap(200)
