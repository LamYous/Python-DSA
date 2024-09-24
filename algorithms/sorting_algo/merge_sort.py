def merge_two_sorted_list(a,b,arr):
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b):
        if b[j] > a[i]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1

def merge_sort(arr):
    if len(arr) <= 1:
        return # its sorted
    
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    # recursion:
    merge_sort(left)
    merge_sort(right)

    #merge:
    merge_two_sorted_list(left,right,arr)
    return arr

arr =[10,3,15,7,8,23,98,29]
print(merge_sort(arr))