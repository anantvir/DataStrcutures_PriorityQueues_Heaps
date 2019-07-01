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

    """ IMPORTANT ! - for ease if implementation, heap tree's array index should start from 1 instead of 0, so None is inserted into TREE[0] position """
    def insert_heap(self,item):
        if len(self.TREE) == 0:                         
            self.TREE.append(None)
        newNode = self.Node(item)
        self.TREE.append(newNode)
        ptr = self.TREE.index(newNode)                  # Get index of last element inserted which will act as pointer to current node

        while ptr > 1:
            par = math.floor(ptr/2)                     # Calculate parent
            if newNode._item < self.TREE[par]._item:    # New item less than parent ?
                self.TREE[ptr] = newNode                # then Insert new item at current pointer position
                return newNode
            self.TREE[ptr] = self.TREE[par]             # New Item greater than parent ? then move down parent to current pointer and update current pointer
            ptr = par                                   # Current pointer = parent --> Move up the pointer
        if ptr == 1:                                    # If pointer becomes root
            self.TREE[ptr] = newNode
        return newNode

    def delete_heap(self):
        last = self.TREE.pop(-1)
        size = len(self.TREE[1:])
        PTR, LEFT, RIGHT = 1,2,3
        while(RIGHT <= size):
            if last._item >= self.TREE[LEFT]._item and last._item >= self.TREE[RIGHT]._item:
                self.TREE[PTR] = last
                return
            if self.TREE[LEFT]._item >= self.TREE[RIGHT]._item:
                self.TREE[PTR] = self.TREE[LEFT]
                PTR = LEFT
            else:
                self.TREE[PTR] = self.TREE[RIGHT]
                PTR = RIGHT
            LEFT = 2*PTR
            RIGHT = LEFT + 1
        
        if LEFT == size and last._item < self.TREE[LEFT]._item:
            self.TREE[PTR] = self.TREE[LEFT]
            PTR = LEFT
            self.TREE[PTR] = last
        return

h = MaxHeap()
h.insert_heap(95)
h.insert_heap(85)
h.insert_heap(70)
h.insert_heap(55)
h.insert_heap(33)
h.insert_heap(30)
h.insert_heap(65)
h.insert_heap(15)
h.insert_heap(20)
h.insert_heap(15)
h.insert_heap(22)
for x in range(1,len(h.TREE)):
    #print(len(h.TREE))
    print(h.TREE[x]._item)
h.delete_heap()
