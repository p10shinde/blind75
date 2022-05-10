# Two Sum
# Given an array of integers, return indices of two numbers such that they add up to a specific target

nums = [2, 7, 11, 15]
nums = [2, 1, 5, 3]
target = 18
target = 4

# Time: O(n)
# Space: O(n) 
def twoSum(nums, target):
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n]=i

print(twoSum(nums, target))