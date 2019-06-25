"""Author - Anantvir Singh, concept reference:= Data Structures in C by Seymour Lipschutz"""

class PriorityQueue:

    class Node:
        def __init__(self,info,priority = None,link = None):
            self.info = info
            self.priority = priority
            self.link = link
    
    def __init__(self):
        self.head = None
        self.current_ptr = None                         # for traversing the list
        self.previous = None                            # used to insert a node between 2 nodes
        self.size = 0
    
    def isEmpty(self):
        return self.size ==0

    def delete_and_process(self):
        if self.head == None:
            raise ValueError('Cannot remove item from empty queue !')
        else:
            node = self.head
            print('Value at node is :',node.info)       # Process the node
            self.head = self.head.link                  # remove node from head
            node.link = None
    
    def insert(self,item,priority):
        if self.head == None:                           # Create head if empty
            newNode = self.Node(item,priority)
            self.head = newNode
            self.previous = newNode
            self.size += 1
        else:
            newNode = self.Node(item,priority)
            self.current_ptr = self.head
            self.previous = self.head
            while self.current_ptr.priority <= priority:    # While priority of current node is less than or equal to priority of new node
                self.previous = self.current_ptr            # Move previous pointer forward
                self.current_ptr = self.current_ptr.link    # Move current pointer forward
                if self.current_ptr == None:                # current pointer becomes None when end of queue os reached. It means insert newNode at last
                    self.previous.link = newNode            # Connect last element of list to newNode
                    self.size += 1
                    return newNode
            if self.current_ptr == self.head:               # Insert node at the front(1st element)
                newNode.link = self.current_ptr
                self.size += 1
                self.head = newNode                         # Make it head
            else:
                newNode.link = self.current_ptr             # Insert newNode between 2 nodes
                self.previous.link = newNode
                self.size += 1
        return newNode

q = PriorityQueue()
q.insert(40,3)
q.insert(20,2)
q.insert(10,3)
q.insert(30,1)
q.insert(30,5)
q.insert(550,1)

        

