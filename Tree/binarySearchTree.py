class binarySearchTree():
    def __init__(self, key) -> None:
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return

        if self.key == data:
            return
        
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = binarySearchTree(data)
        
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = binarySearchTree(data)

#     4
#   /   \
#  2     6
# / \   / \
#1   3 5   7

    def preOrder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preOrder()
        if self.rchild:
            self.rchild.preOrder()

    def inOrder(self):
        if self.lchild:
            self.lchild.inOrder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inOrder()
        
    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()
        if self.rchild:
            self.rchild.postOrder()
        print(self.key, end=" ")

    def search_node(self, item):
        if self.key == item:
            print(f"'{item}' is faund.")
            return
        
        if self.key > item:
            if self.lchild:
                self.lchild.search_node(item)
            else:
                print(f"'{item}' is not present in tree.")
        else:
            if self.rchild:
                self.rchild.search_node(item)
            else:
                print(f"'{item}' is not present in tree.")

    def delete_node(self, item, curr): 
        if self.key is None: 
            print("Tree is Empty!") 
            return
        
        if self.key > item: 
            if self.lchild: 
                self.lchild = self.lchild.delete_node(item, curr) 
            else: 
                print("Given Node is Not present in the tree!")
                
        elif self.key < item: 
            if self.rchild:
                self.rchild = self.rchild.delete_node(item, curr) 
            else:
                print(f"Given Node is Not present in the tree!")

        # self.key == item       
        else: 

            """Given Node hase one child"""    
            if self.lchild is None:  
                temp = self.rchild 
                if self.key == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    return
                self = None 
                return temp 
            
            if self.rchild is None:
                temp = self.lchild
                if self.key == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    return
                self = None 
                return temp
            
            """Given Node two childs"""
            node = self.rchild 
            while node.lchild: 
                node = node.lchild
            self.key = node.key  
            self.rchild = self.rchild.delete_node(node.key, curr) 
        return self 
    
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print(f"Node with smallest key is: {current.key}")

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print(f"Node with maximum key is: {current.key}")

def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)

#-------------------
root = binarySearchTree(4)

root.insert(2)
root.insert(5)
root.insert(7)
root.insert(6)
root.insert(1)
root.insert(3)
root.preOrder()
print()
root.inOrder()
print()
root.postOrder()
print()
root.search_node(3)

#delete item:
if count(root) > 1:
    root.delete_node(6, root.key)
    root.inOrder()
else:
    print("can't perform deletion operation!")


print()
root.min_node()
root.max_node()
