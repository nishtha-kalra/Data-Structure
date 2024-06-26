'''
Two Sum Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
nums = [2, 7, 11, 15]
target = 9
Output = [0, 1]
'''

# return numbers summing to taget
def twoSumNums(nums, target):
    for num in nums:
        diff = target - num
        if diff in nums:
            return ([num, diff])

# return indices of numbers summing to target
def twoSumIndices(nums, target):
    num_index = {}
    for i in range(len(nums)):
        num = nums[i]
        diff = target - num
        if diff in num_index:
            diff_index = num_index[diff]
            return ([diff_index, i])
        num_index[num] = i
        
            
nums = [2, 7, 4, 5, 11]
target = 9
outputNum = twoSumNums(nums, target)
print(outputNum)
outputIndex = twoSumIndices(nums, target)
print(outputIndex)
