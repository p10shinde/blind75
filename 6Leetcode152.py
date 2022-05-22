# Maximum product subarray

# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product

# Linear
# Time: O(n)
# Space: O(1)

nums = [2,3,-2,4] #6
nums = [-2, 0, -1] #0
nums = [0,2] #2


maxProd = max(nums)
curMin, curMax = 1, 1

for n in nums:
    if n == 0:
        curMin, curMax = 1, 1
        continue

    tmp = curMax * n
    curMax = max(curMax * n, curMin * n, n)
    curMin = min(tmp, curMin * n, n)

    maxProd = max(maxProd, curMin, curMax)

print(maxProd)
