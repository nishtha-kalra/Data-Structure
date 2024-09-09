'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = ''
        for letter in s:
            if letter.isalnum():
                phrase = phrase + letter.lower()
        return (phrase == phrase[::-1])
        
