class treeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTravers(node):
    if node is None:
        return
    print(node.data, end=",")
    preOrderTravers(node.left)
    preOrderTravers(node.right)

def inOrderTravers(node):
    if node is None:
        return
    inOrderTravers(node.left)
    print(node.data, end=",")
    inOrderTravers(node.right)

def postOrderTravers(node):
    if node is None:
        return
    postOrderTravers(node.left) 
    postOrderTravers(node.right)
    print(node.data, end=",")

root = treeNode("R")
nodeA = treeNode("A")
nodeB = treeNode("B")
nodeC = treeNode("C")
nodeD = treeNode("D")
nodeE = treeNode("E")
nodeF = treeNode("F")
nodeG = treeNode("G")
 
root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print("\n---Binary Tree---")
print("root.right.left.data:",root.right.left.data)

print("\n---preOrderTravers---")
preOrderTravers(root)

print("\n---inOrderTravers")
inOrderTravers(root)

print("\n---postOrderTravers---")
postOrderTravers(root)