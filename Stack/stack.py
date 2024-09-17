class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, item):
        if len(self.stack) == self.capacity:
            print("Stack is Full.")
        else:
            self.stack.append(item)
            print(f"{item} is pushed to Stack.")
    
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is Empty.")
        else:
            self.stack.pop()
            print("Pop method is done.")

    def isFull(self):
        if len(self.stack) == self.capacity:
            print("Stack is Full.")
        else:
            print("Stack is not Full.")

    def isEmpty(self):
        if len(self.stack) == 0:
            print("Stack is Empty.")
        else:
            print("Stack is not Empty.")

        
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is Empty.")
        else:
            print(f"The Peek Element is: {self.stack[-1]}")

    def stackSize(self):
        print(f"Stack Size: {len(self.stack)}")

stack = Stack(5)
stack.isEmpty()

stack.push(12)
stack.push(10)
stack.push(5)
stack.push(8)
stack.isFull()
stack.peek()
stack.stackSize()
stack.push(1)
stack.isFull

stack.pop()
stack.pop()
stack.pop()
stack.peek()
stack.pop()
stack.pop()
stack.isEmpty()
