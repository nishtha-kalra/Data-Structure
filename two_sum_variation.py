'''
Find all pairs that sum to target
Input: nums = [1, 2, 3, 4, 3, 5, 6], target = 6
Output: [(1, 5), (2, 4), (3, 3)]
'''

def all_sum(nums, target):
    seen = {}
    result = []
    for num in nums:
        complement = target - num
        if complement in seen and seen[complement] > 0:
            result.append((complement, num))
            seen[complement] -= 1
        else:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
    print(result)

nums = [1, 2, 3, 4, 3, 5, 6]
target = 6
all_sum(nums, target)
