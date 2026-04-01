class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(24)
node3 = Node(33)
node4 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

currentNode = node1
startNode = node1
print(currentNode.data , end="->")
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data , end="->")
    currentNode = currentNode.next

print("....")    

