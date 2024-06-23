
'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
 ["ate","eat","tea"],
 ["nat","tan"],
 ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

def anagrams(input):
    sorted_dict = {}
    for word in input:
        sorted_word = ''.join(sorted(word))
        if sorted_word in sorted_dict:
            sorted_dict[sorted_word].append(word)
        else:
            sorted_dict[sorted_word] = [word]
    output = list(sorted_dict.values())
    return (output)
    
input = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = anagrams(input)
print(output)
'''
time complexity = 
n = no of words in the input
k = average length of a word
to sort a word = O(klogk)
since there are n words that are sorted, total complexity = O(n.klogk)
inserting all strings in dictionary = O(n)
constructing the output = O(n)
combining all time compexities = O(n.klogk)
space complexity = 
for dictionary, storing n keys for average length of k = O(n.k)
for ouput, sorting n words with avg length of k = O(n.k)
total space complexity = O(n.k)
'''
