def binary_search(arr, item, left, right):
    while right >=left:
        mid = left+ (right - left) // 2

        if arr[mid] == item:
            return mid
        
        elif arr[mid] > item:
            right =  mid - 1

        else:
            left = mid + 1

    return None

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    item = 2
    left = 0
    right = len(arr)-1

    result = binary_search(arr, item, left, right)

    if result is None:
        print(f"{item} is not present.")
    else:
        print(f"{item} is present at index {result}")
