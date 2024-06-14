
# find all substrings for an array/string

def substring(arr):
    n = len(arr)
    sub = []
    for i in range(n):
        for j in range(i+1, n+1):
            sub.append(arr[i:j])
    return sub

a = [1,2,3,4,5]
ans = substring(a)
print(ans)
