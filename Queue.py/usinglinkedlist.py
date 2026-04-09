class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.lengh = 0

    def enqueue(self,element):
        new_node = Node(element)
        

   