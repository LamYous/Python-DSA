class Array():
    def __init__(self):
        self.array = []

    def addItem(self, item):
        self.array.append(item)
        print(f"{item} is added to Array.")

    def insert_at_specific_index(self, item, index):
        self.array.insert(index, item)
        print(f"{item} has been inserted at index {index}.")
    
    def traversal(self):
        if len(self.array) == 0:
            print("Array is Empty.")
        else:
            for i in self.array:
                print(i, end=" ")

    def arraySize(self):
        print(f"Array Size: {len(self.array)}")

    def delete_item(self, item):
        if len(self.array) == 0:
            print("Array is Empty.")
        else:
            if item in self.array:
                self.array.remove(item)
                print(f"{item} element has been deleted.")
            else:
                print(f"{item} not present in the array.")

    def delete_last_item(self):
        if len(self.array) == 0:
            print("Array is Empty.")
        else:
            self.array.pop()
            print("The last item has been deleted.")
                

    def search(self, item):
        for i in range(len(self.array)):
            if item == self.array[i]:
                print(f"{item} is present at index {i}.")
        if item not in self.array:
            print(f"{item} is not present in the array.")


arr = Array()

arr.addItem(10)
arr.addItem(12)
arr.addItem(8)

arr.traversal()
arr.insert_at_specific_index(5, 1)
arr.traversal()

arr.delete_item(12)

arr.arraySize()