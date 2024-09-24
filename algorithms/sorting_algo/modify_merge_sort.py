def merge_sort(arr):
    if len(arr) > 1: 
        l_arr = arr[:len(arr)//2]
        r_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(l_arr)
        merge_sort(r_arr)

        #merge
        i=0 #left array index 
        j=0 #right array index
        k=0 #merge array index

        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] < r_arr[j]:  
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
            k += 1
        
        #Checking if any element was left
        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1

        #Checking if any element was right
        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1
    return arr
            
arr = [2,1,3,4,7,6,9]   
print(arr)  
merge_sort(arr)
print(arr) 