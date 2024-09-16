'''
left rotate an array
Input: a = [1, 2, 3, 4, 5] and d = 4
Output: [5, 1, 2, 3, 4] (after 4 left rotations)
'''
def rotLeft(a, d):
    first_half = a[d:]
    second_half = a[:d]
    return (first_half + second_half)

a = [1, 2, 3, 4, 5]
d = 4
print(rotLeft(a, d))
