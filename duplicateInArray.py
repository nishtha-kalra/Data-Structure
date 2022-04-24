#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:39:42 2022

@author: nishtha

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]

"""

def duplicate1(arr):
    common = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
               common.append(arr[i])
    print (common)
    
def duplicate2(arr):
    seen = set()
    common = []
    for element in arr:
        if element in seen:
            common.append(element)
        else:
            seen.add(element)
    print (common)
        
def duplicate3(arr):
    visited = dict.fromkeys(arr, False)
    duplicate = []
    for i in range(len(arr)):
        if visited[arr[i]]:
            duplicate.append(arr[i])
        else:
            visited[arr[i]] = True
    print(duplicate)
print ("finding duplicate in array")
print ("first method with nested loop")
arr = [4,3,2,7,8,2,3,1]
duplicate1(arr)
print ("using set")
duplicate2(arr)
print ("creating a visited map/dict")
duplicate3(arr)