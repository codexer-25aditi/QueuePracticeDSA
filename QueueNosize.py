class queue:
    def __init__(self):
        self.qu=[]
    def __str__(self):
        values=[str(x) for x in self.qu]
        return ' '.join(values)
    def isEmpty(self):
        if self.qu==[]:
            return True
        else:
            return False

    def enqueue(self,v):
        self.qu.append(v)
        return f"The {v} is enqueued"
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            self.qu.pop(0)
            return "The queue is dequeued"
    def peek(self):
        return self.qu[0]
customs=queue()
print(customs.isEmpty())
print(customs.enqueue(1))
print(customs.enqueue(2))
print(customs.enqueue(3))
print(customs.enqueue(4))
print(customs)
print(customs.dequeue())
customs.dequeue()
print(customs)
print(customs.peek())

