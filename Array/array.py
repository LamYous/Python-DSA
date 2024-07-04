class Array:
    def __init__(self) -> None:
        self.arr = []

    def add_item(self,item):
        return self.arr.append(item)
    
    def insert_item(self, item, index):
        return self.arr.insert(index, item)
    
    def traversal(self):
        if len(self.arr) == 0:
            print("Array is Empty.")
        else:
            for i in range(len(self.arr)):
                print(self.arr[i], end=" ")
        print()

    def arr_size(self):
        print(len(self.arr))
    
    def delete_item(self, item):
        if item in self.arr:
            return self.arr.remove(item)
        else:
            print("item is not present in the array.")

    def delete_last_item(self):
        self.arr.pop()
        return "The last item has been deleted!"


    def search(self, item):
        for i in self.arr:
            if item == i:
                print(f"{item} is present at index {self.arr[i]}.")
        if item not in self.arr:
            print(f"{item} is not faund.")



arr = Array()
arr.add_item(1)
arr.add_item(2)
arr.add_item(3)
arr.traversal()
arr.insert_item(0,1)
arr.traversal()
arr.arr_size()
arr.delete_item(10)
arr.traversal()
arr.search(10)

