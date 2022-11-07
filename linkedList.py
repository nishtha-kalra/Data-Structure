'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #dummyHead = ListNode(0)
        root = ListNode(0)
        result = root
        carry = 0
        #print(l1)
        #print(l2)
        while l1 != None or l2 != None or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            colSum = l1Val + l2Val + carry
            result.next = ListNode(colSum % 10)
            result = result.next
            carry = colSum // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return root.next  
