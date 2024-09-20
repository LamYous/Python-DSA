def binary_search(arr, item, left, right):
    if right >= left:
        mid = left + (right - left) // 2

        if arr[mid] ==  item:
            return mid

        elif arr[mid] > item:
            return binary_search(arr, item, left, mid-1)
        
        else:
            return binary_search(arr, item, mid+1, right)
        
    return None
        
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    item = 0
    result = binary_search(arr, item, 0, len(arr)-1)

    if result is None:
        print(f"{item} is not present in array.")
    else:
        print(f"{item} is presnet at index {result}")