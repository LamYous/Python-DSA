class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None    

    def add_node(self,data):
        self.data = Node(data)
        if self.head is None:
            newNode = Node(data)
            self.head = newNode

        else:
            newNode= Node(data)
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def insert_at_begenning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_at_specified_node(self, posetion, data):
        newNode = Node(data)
        a = self.head
        for i in range(1, posetion-1):
            a = a.next
        newNode.next = a.next
        a.next = newNode

    def delete_at_bg(self):
        a = self.head
        self.head = a.next
        a.next = None

    def delete_at_end(self):
        #condition1: the linked list has more than One Node
        if self.head.next:
            prev = self.head
            a = self.head.next
            while a.next:
                a = a.next
                prev = prev.next
            prev.next = None
            
        #condition2: the linked list has one Node(self.head == last Node)
        else:
            self.head = None
    

    def delete_at_particular_node(self,posetion):
        prev = self.head
        a = self.head.next

        if posetion != 1:
            for i in range(1 ,posetion-1):
                a = a.next
                prev = prev.next
            prev.next = a.next
            a.next = None
        #if posetion == 1 (first Node)
        else:
            a = self.head
            self.head = a.next
            a.next = None

    def traversal(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next
            print()

            
        
            
        
# n1 = Node(data= 10)
sll = LinkedList()
# print(sll.head)
sll.add_node(4)
sll.add_node(10)
sll.traversal()

sll.insert_at_begenning(1)
sll.traversal()

sll.insert_at_specified_node(posetion=2,data=2)
sll.traversal()

# # sll.delete_at_bg()
# # sll.traversal()

# # sll.delete_at_end()
# # sll.traversal()

sll.delete_at_particular_node(posetion=1)
sll.traversal()

# sll.search(1)
# sll.search(10)
# sll.search(100)