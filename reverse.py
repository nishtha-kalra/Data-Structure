#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 19:01:15 2022

@author: nishtha

Reverse a string
"""

    
def reverse1(string):
    print(string[::-1])

def reverse2(string):
    '''
    If you pass a string to reversed(), you get an iterator that yields characters in reverse order.
    t doesn’t create a new reversed string but reads characters backward from the existing one. 
    This behavior is fairly efficient in terms of memory consumption and can be a fundamental win in some contexts and situations, such as iteration.
    You can use the iterator that you get from calling reversed() directly as an argument to .join()
    '''
    print("".join(reversed(string)))

def reverse3(string):
    rev = ""
    for char in string:
        rev = char + rev
    print(rev)
    
print("slicing way:")
string = "The quick brown 狐 jumped over the lazy 犬 The quick brown 狐 jumped over the lazy 犬"
reverse1(string)
print("reversed and join way")
reverse2(string)
print("using loop")
reverse3(string)