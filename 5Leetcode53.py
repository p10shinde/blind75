# Maximum subarray
# Given an integer array nums, find the contaguous subarray (containing at least one number) which
# has the largest sum and return its sum.

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Linear
# Time: O(n)
# Space: O(1)
maxSub = nums[0]
currsum = 0

for n in nums:
    if currsum < 0:
        currsum = 0
    currsum += n
    maxSub = max(maxSub, currsum)
print(maxSub)