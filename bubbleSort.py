def bubblesort(arr):
    length = len(arr)
    swapped = False
    for i in range(length):
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # if there hasn't been any swaps in above loop then the list is already sorted
        if not swapped:
            break
                
arr = [1,6,3,7,2,200,4]
print('before sorting:', arr)
bubblesort(arr)
print('after sorting:', arr)
