'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''
class Solution:
    def strStr1(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    # alt way without using find()
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)
        len_needle = len(needle)
        for i in range(len_haystack-len_needle+1):
            if haystack[i:i+len_needle] == needle:
                return (i)
        return (-1)
        
