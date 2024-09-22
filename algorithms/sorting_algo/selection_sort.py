def selection_sort(arr):
    for i in range(len(arr)):
        min_element = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_element]:
                min_element = j #update the min_element value
        if min_element != i:
            arr[min_element], arr[i] = arr[i], arr[min_element]
    return arr

 

arr = [64, 25, 12, 22, 11]
print(arr)
print(selection_sort(arr))