class Queue:
    def __init__(self):
        self.queue = []
    def Enqueue(self,data):
        return self.queue.append(data)

    def display(self):
        print(self.queue)

    def Dequeue(self):
        return self.queue.pop(0)
    
    def Size(self):
        print(len(self.queue))
    
    def IsEmpty(self):
        if len(self.queue) == 0:
            print("Queue is Empty!")
        else:
            print("Queue is not Empty!")

q = Queue()
q.display()
q.IsEmpty()

q.Size()

q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)

q.display()
q.Size()

q.Dequeue()
q.Dequeue()
q.display()
q.IsEmpty()
q.Size()
