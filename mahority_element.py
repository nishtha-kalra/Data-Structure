class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_of_digits = {}
        for digit in nums:
            if digit in count_of_digits:
                count_of_digits[digit] += 1
            else:
                count_of_digits[digit] = 1
            if count_of_digits[digit] > len(nums)/2:
                return(digit)
        return (0) # not found
    # alternative way
    def majorityElement1(self, nums: List[int]) -> int:
        nums_set = list(set(nums))
        n = len(nums)/2
        for digit in nums_set:
            count = nums.count(digit)
            if count > n:
                return (digit)
