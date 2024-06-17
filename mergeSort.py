def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
    
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
        
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1
            
arr = [8,5,4,3,7,1,6,2]
print('before sorting:', arr)
merge_sort(arr)
print('after sorting:', arr)
