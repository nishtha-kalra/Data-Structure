
# Online Python - IDE, Editor, Compiler, Interpreter

def binarySearchIterative(arr, search):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == search:
            return True
        elif search < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False

def binarySearchRecursive(arr, search, left, right):
    mid = (left + right) // 2
    if left > right:
        return False
    if arr[mid] == search:
        return True
    elif search < arr[mid]:
        return binarySearchRecursive(arr, search, left, mid - 1)
    else:
        return binarySearchRecursive(arr, search, mid + 1, right)
    
arr = [2,3,8,10,20,45,88]
search = 45
ans = binarySearchIterative(arr, search)
print (ans)
ans = binarySearchRecursive(arr, search, 0, len(arr) - 1)
print(ans)
