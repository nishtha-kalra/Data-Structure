#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 16:41:53 2022

@author: nishtha

Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

def powerset(arr):
    output = [[]]
    for num in arr:
        output += [curr + [num] for curr in output]
    print (output)

print("print powerset")
arr = [1,2,3]
powerset(arr)