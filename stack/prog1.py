stack = []

stack.append("A")
stack.append("B")
stack.append("C")
print("stack",stack)

element = stack.pop()
print("element", element)

topelement = stack[-1]
print("topelement", topelement)

isEmpty = not bool(stack)
print("isempty", isEmpty)

print("size",len(stack))

