class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)

class LL:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

class queue:
    def __init__(self):
        self.Ll=LL()

    def __str__(self):
        value=[str(x) for x in self.Ll]
        return "".join(value)
    def isEmpty(self):
        if self.Ll.head==None and self.Ll.tail==None:
            return True
        else:
            return False
    def enqueue(self,value):
        new_node=Node(value)
        if self.Ll.head==None:
            self.Ll.head=new_node
            self.Ll.tail=new_node
        else:
            self.Ll.tail.next=new_node
            self.Ll.tail=new_node
    def dequeue(self):#fifo
        if self.isEmpty():
            print("The queue is empty")
        elif self.Ll.head==self.Ll.tail:
            self.Ll.head=None
            self.Ll.tail=None
        else:
            self.Ll.head=self.Ll.head.next
    def peek(self):
        return self.Ll.head.value



custom=queue()
custom.enqueue(1)
custom.enqueue(2)
custom.enqueue(3)
custom.enqueue(4)
print(custom)
custom.dequeue()
print(custom.peek())

print(custom)









