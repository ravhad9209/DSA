Queue = []

Queue.append("A")
Queue.append("B")
Queue.append("C")
print("Queues:", Queue)

element = Queue.pop()
print("pop:",element)

topElement = Queue[-1]
print("peek:",topElement)

isEmpty = not bool(Queue)
print("isEmpty:",isEmpty)

print("size:",len(Queue))