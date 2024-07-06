class binarySearchTree():
    def __init__(self, key) -> None:
        self.key = key
        self.lchild = None
        self.rchlid = None

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
            if self.rchlid:
                self.rchlid.insert(data)
            else:
                self.rchlid = binarySearchTree(data)

#     4
#   /   \
#  2     6
# / \   / \
#1   3 5   7

    def preOrder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preOrder()
        if self.rchlid:
            self.rchlid.preOrder()

    def inOrder(self):
        if self.lchild:
            self.lchild.inOrder()
        print(self.key, end=" ")
        if self.rchlid:
            self.rchlid.inOrder()
        
    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()
        if self.rchlid:
            self.rchlid.postOrder()
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
            if self.rchlid:
                self.rchlid.search_node(item)
            else:
                print(f"'{item}' is not present in tree.")

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
root.search_node(7)

root.inOrder()