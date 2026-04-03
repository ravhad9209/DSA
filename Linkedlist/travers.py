class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traversAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end='->')
        currentNode = currentNode.next
    print("null") 

node1 = Node(12)
node2 = Node(53)
node3 = Node(8)
node4 = Node(90)

node1.next = node2
node2.next = node3
node3.next = node4

traversAndPrint(node1)


