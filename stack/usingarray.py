class Stack:
    def __init__(self):
        self.stack = []
    
    #Push
    def push(self, element):
        self.stack.append(element)
    
    #Pop
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()    
    
    #Peek
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]
    
    #isEmpty
    def isEmpty(self):
        return len(self.stack) == 0
    
    #Size
    def size(self):
        return len(self.stack)
    
myStack = Stack()

myStack.push("A")
myStack.push("B")
myStack.push("c")
print("stack:",myStack.stack)

print("push:", myStack.pop())
print("peek:",myStack.peek())
print("isEmpty:",myStack.isEmpty())
print("Size:",myStack.size())