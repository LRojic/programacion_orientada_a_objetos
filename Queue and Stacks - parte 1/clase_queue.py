class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


q = Queue()

q.enqueue(5)
q.enqueue(10)

print(q.dequeue())
print(q.peek())