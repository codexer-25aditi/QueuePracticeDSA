class Queue:
    def __init__(self,maxSize):
        self.items=maxSize*[None]
        self.maxSize=maxSize
        self.top=-1
        self.start=-1

    def __str__(self):
        values=[str(x) for x in self.items]
        return " ".join(values)

    def isEmpty(self):
        if self.top==-1 and self.start==-1:
            return True
        else:
            return False
    def isFull(self):
        if self.top+1==self.maxSize:
            return True
        elif self.top+1==self.start:
            return True
        else:
            return False
    def enQueue(self,value):
        if self.isFull():
            return "Cannot be more inserted"
        else:
            if self.top+1==self.maxSize:
                self.top=0
            else:
                self.top=self.top+1
                if self.top==-1:
                    self.top=0
                self.items[self.top]=value


    def deQueue(self):
        if  self.isEmpty():
            return "The Queue is Empty"
        else:
            first=self.items[self.start]
            startt=self.start
            if self.start+1==self.maxSize:
                self.start=0
            elif self.start==self.top:
                self.start=-1
                self.top=-1
            else:
                self.start=self.start+1
            self.items[startt]=None
            return first
    def delete(self):
        self.items=self.maxSize*[None]
        self.start=-1
        self.top=-1
custom=Queue(3)
print(custom.isEmpty())
print(custom.isFull())
custom.enQueue(1)
custom.enQueue(2)
custom.enQueue(3)
print(custom.deQueue())
custom.enQueue(4)
print(custom)





