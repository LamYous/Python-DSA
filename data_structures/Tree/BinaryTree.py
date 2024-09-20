class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = BinaryTree(value=data)
                else:
                    self.left.insert(data)
            elif data > self.value:
                if self.right is None:
                    self.right =BinaryTree(value=data)
                else:
                    self.right.insert(data)
            else:
                self.value = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value, end=" ")
        if self.right:
            self.right.PrintTree()

root = BinaryTree(100)
root.insert(50)
root.insert(55)
root.insert(60)
root.insert(20)
root.insert(52)
root.PrintTree()
