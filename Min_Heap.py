"""Author -  Anantvir Singh, Concept Reference - Data Structures in C by Seymour Lipschutz"""
import math
class Min_Heap:
    class Node:
        def __init__(self,info,parent = None,left = None,right = None):
            self.info = info
            self.parent = parent
            self.left = left
            self.right = right
    
    def __init__(self):
        self.TREE = []
    
    """IMPORTANT ! --> For easier implementation, array TREE[0] contains None and index starts from 1"""
    def insert_heap(self,item):
        if len(self.TREE) == 0:
            self.TREE.append(None)
        newNode = self.Node(item)
        self.TREE.append(newNode)
        ptr = self.TREE.index(newNode)
        while ptr > 1:
            par = math.floor(ptr/2)
            if newNode.info >= self.TREE[par].info:
                self.TREE[ptr] = newNode
                return newNode
            self.TREE[ptr] = self.TREE[par]
            ptr = par
        if ptr == 1:
            self.TREE[ptr] = newNode
        return newNode


h = Min_Heap()

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