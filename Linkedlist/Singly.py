class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(8)
node2 = Node(13)
node3 = Node(5)
node4 = Node(43)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data , end='->')
    currentNode = currentNode.next
print("null")    
