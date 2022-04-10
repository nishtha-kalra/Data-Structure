#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 20:29:09 2022

@author: nishtha

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

def zeros1(arr):
    count_of_zeros = 0
    new_arr = []
    for a in arr:
        if a == 0:
            count_of_zeros = count_of_zeros + 1
        else:
            new_arr.append(a)
    for zero in range(count_of_zeros):
        new_arr.append(0)
    print(new_arr)
            

'''
In-place means we should not be allocating any space for extra array.
But we are allowed to modify the existing array.
A two-pointer approach could be helpful here.
The idea would be to have one pointer for iterating the array and another pointer
that just works on the non-zero elements of the array.
0  1  0  3  12

p1 = 4
p2 = 3
arr = 1 3 12 
'''
def zeros2(arr):
    p2 = 0
    for p1 in range(len(arr)):
        if arr[p1] != 0:
            arr[p2] = arr[p1]
            p2 = p2 + 1
    for i in range(p2, len(arr)):
        arr[i] = 0
    print(arr)
    
array = [0,1,0,3,12]
print("first way that is direct, with 2 loops")
zeros1(array)
print("pointer way:")
zeros2(array)