def linear_search(arr, item):

    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return None


if __name__ == '__main__':
    arr = [1,3,9,12,82,9]
    item = 12

    result = linear_search(arr,item)
    if result is None:
        print(f"{item} is not present is the array.")
    else:
        print(f"{item} is present in index {result}.")