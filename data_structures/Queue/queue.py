class Queue():
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def enqueue(self, item):
        if len(self.queue) == self.capacity:
            print("Queue is Full.")
        else:
            self.queue.append(item)
            print(f"{item} is enqueued to queue.")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is aleardy Empty.")
        else:
            self.queue.pop(0)
            print("Dequeue method is done.")

    def isEmpty(self):
        if len(self.queue) == 0:
            print('Queue is Empty.')
        else:
            print('Queue is not Empty.')
        
    def isFull(self):
        if len(self.queue) == self.capacity:
            print("Queue is Full.")
        else:
            print("Queue is not Full.")

    def queueSize(self):
        print(f"Queue Size: {len(self.queue)}")
    
    def que_front(self):
        print(f"The element at the front: {self.queue[0]}")
    

    def que_rear(self):
        print(f"The element at the front: {self.queue[-1]}")
        


q = Queue(capacity = 6)

q.enqueue(10)
q.enqueue(12)
q.enqueue(5)
q.enqueue(8)
q.isFull()

q.que_rear()
q.que_front()

q.queueSize()

q.dequeue()

q.isEmpty()