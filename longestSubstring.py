'''
Find the Longest Substring Without Repeating Characters
s = "abcabcbb"
Output: 3
'''

def longestSubstring(string):
    substring = []
    max_substring_length = 0
    for char in string:
        if char in substring:
            substring_length = len(substring)
            max_substring_length = max(substring_length, max_substring_length)
            substring = []
            substring.append(char)
        else:
            substring.append(char)
    max_substring_length = max(len(substring), max_substring_length)
    return (max_substring_length)

string = "abcdabddcabf"
output = longestSubstring(string)
print(output)
