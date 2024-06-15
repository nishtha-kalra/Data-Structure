# basic python operations
from functools import reduce

def twoDarray():
    arr = [[1,2,1], [2,3,6], [4,5,2]]
    '''
    1 2 1
    2 3 6
    4 5 2
    '''
    print('second row:', arr[1]) 
    print('element in thirs row third col:', arr[2][2])
  
def minmax(arr):
    print('min number:', min(arr))
    print('max number:', max(arr))

def slicing(arr):
    print('array from 1st to 3rd index:', arr[1:4])
    
def sorting(arr):
    print('new array with sorted element:', sorted(arr))
    print('new array with sorted element in desc order:', sorted(arr, reverse=True))
    arr.sort()
    print('same array sorted:', arr)

def functional(arr):
    func = lambda x: x ** 2
    squared = list(map(func, arr))
    print('squaring using map:', squared)
    
    sum_arr = reduce(lambda x, y: x + y, arr)
    print('sum of array using reduce:', sum_arr)
    
    even = list(filter(lambda x: x% 2 == 0, arr))
    print('find even numbers using filter:', even)
    
    print('adding index using enumerate')
    for index, a in enumerate(arr, start=1):
        print(f'{index}: {a}')
        
    arr2 = ['a', 'b', 'c']
    print('aggregate:', arr + arr2)
    print('agrregate using zip:', list(zip(arr, arr2)))
    
    comprehension = [x**2 for x in arr]
    print('cooncise way to create squared list:', comprehension)

def hashmap():
    fruits = {
        1: 'apple',
        2: 'banana',
        3: 'mango'
    }
    print('fruits:', fruits)
    
    print('accessing value in hashmap:', fruits[2])
    
    fruits[4] = 'melon'
    print('new value of fruits after addition:', fruits)
    
    fruits[3] = 'grapes'
    print('new value of fruits after updation:', fruits)
    
    del fruits[1]
    print('new value of fruits after deletion:', fruits)
    
    popped = fruits.pop(2)
    print("fetching 2nd element:", popped)
    print('fruits after popping last element:', fruits)
    
    print('iterating over keys:')
    for key in fruits:
        print(key)
        
    print('iterating over values:')
    for value in fruits.values():
        print(value)
        
    print('iterating over key and values:')
    for key, value in fruits.items():
        print(f'key: {key}, value: {value}')
    
arr = [9,2,1,-3,4]
print('python 3 operations')
print('2D array operations')
twoDarray()
print('min and max')
minmax(arr)
print('slicing')
slicing(arr)
print('sorting')
sorting(arr)
print('functional operations')
functional(arr)
print('dictionary/hashmap operations')
hashmap()
