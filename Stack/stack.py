class Stack:
    def __init__(self) -> None:
        self.stack = []

    def add_item(self, item):
        return self.stack.append(item)
    
    def pop_item(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            element_poped = self.stack.pop()
            print("Element poped: ",element_poped)

    def stack_size(self):
        return len(self.stack)
    
    def my_stack(self):
        if len(self.stack) == 0:
            print("Stack is Empty.")
        else:
            print(self.stack)
    
stack = Stack()
stack.add_item(1)
stack.my_stack()
stack.add_item(2)
stack.add_item(3)
stack.add_item(4)
stack.my_stack()
stack.pop_item()
stack.pop_item()
stack.pop_item()
stack.pop_item()
stack.pop_item()