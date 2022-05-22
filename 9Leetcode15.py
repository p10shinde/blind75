# 3Sum

# Given an array nums of n integers, are there elements a,b,c in nums such that
# a + b + c = 0? Find all unique triplets in the array which gives the sum of zero

# Time: O(nlog n) + O(n2) => O(n2)
# Space: O(1) or O(n)


nums = [-1, 0, 1, 2, -1, -4]
res = []

nums.sort()

for i, value in enumerate(nums):
    if i > 0 and value == nums[i-1]:
        continue

    l, r = i + 1, len(nums) - 1
    while l < r:
        threeSum = value + nums[l] + nums[r]

        if threeSum > 0:
            r -= 1
        elif threeSum < 0:
            l += 1
        else:
            res.append([value, nums[l], nums[r]])
            l += 1
            while nums[l] == nums[l - 1] and l < r:
                l += 1
print(res)