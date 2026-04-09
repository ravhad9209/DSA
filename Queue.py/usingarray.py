class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queues is Empty"
        return self.queue.pop()

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[-1]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

myQueue = Queue()

myQueue.enqueue("A")
myQueue.enqueue("B")
myQueue.enqueue("C")
print("enqueue:",myQueue.queue)

print("dequeue:",myQueue.dequeue())
print("peek:",myQueue.peek())
print("isEmpty:",myQueue.isEmpty())
print("size:",myQueue.size())