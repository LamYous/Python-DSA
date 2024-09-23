def bubble_sort(arr):
    for i in range(len(arr)):
        swapping = False 

        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]=  arr[j+1], arr[j] 
                swapping = True 
        if swapping == False:
            break
    return arr
    
arr = [2,7,9,4,8,90,1,0]
print(bubble_sort(arr))
