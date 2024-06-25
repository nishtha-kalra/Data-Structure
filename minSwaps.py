'''
Asked in amazon online assessment:
I have an array. We need to swap elements in the array such that the first element is the smallest and last element is the largest. We can only swap adjacent element. Calculate how many swaps will be required.
For example : input = [2,4,3,1,6] output = 3 because
 first swap = [2,4,1,3,6] 
second swap = [2,1,4,3,6]
third swap = [1,2,4,3,6] 
the smallest number 1 is at first position now and largest number 6 is at last position
'''

def swapNumbers(arr):
    min_index = arr.index(min(arr))
    swaps = 0
    
    while min_index > 0:
        arr[min_index], arr[min_index-1] = arr[min_index-1], arr[min_index]
        swaps += 1
        min_index -= 1
    max_index = arr.index(max(arr))
    while max_index < len(arr) - 1:
        arr[max_index], arr[max_index+1] = arr[max_index+1], arr[max_index]
        max_index += 1
        swaps += 1
    return (swaps)
    
arr = [2,4,3,1,6]
output = swapNumbers(arr)
print(output)
arr1 = [3,2,1]
output1 = swapNumbers(arr1)
print(output1)
