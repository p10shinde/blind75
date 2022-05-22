# Search in Rotated Sorted Array

# Suppose an array sorted in ascending order is rotated at some oipvot unknown
# to you beforehand, you are given a target value to search. If found in the array
# return index, else -1

# Time: O(log n)
# Space: O(1)

nums = [4,5,6,7,0,1,2]
target = 0

l,r = 0, len(nums) - 1
foundIndex = 0
while l <= r:
    m = (l + r) // 2

    if target == nums[m]:
        foundIndex = m
        break

    # we are in left sorted portion
    if nums[l] <= nums[m]:
        if target > nums[m] or target < nums[l]:
            l = m + 1
        else:
            r = m - 1
    # we are in right sorted portion
    else:
        if target < nums[m] or target >  nums[r]:
            r = m - 1
        else:
            l = m + 1

print(foundIndex)