class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def LowestValuePrint(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

node1 = Node(8)
node2 = Node(21)
node3 = Node(12)
node4 = Node(35)

node1.next = node2
node2.next = node3
node3.next = node4

print("The Lowest Value Given Linked list:",LowestValuePrint(node1))
