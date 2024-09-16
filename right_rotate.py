'''
rotate an array to right by given d elements
a = [1,2,3,4,5]
d = 2
[1,2,3,4,5] -> [5,1,2,3,4] -> [4,5,1,2,3]
'''

def rotate_right(a, d):
    d = d % len(a)
    # last d elements of the array
    first_half =  a[-d:]
    # elements before the last d elements
    second_half = a[:-d]
    return (first_half+second_half)

a = [1,2,3,4,5]
d = 2
rotated = rotate_right(a, d)
print(rotated)