# Find minimum in rotated sorted array

# suppose an array of length n sorted in ascending order is rotated
# between 1 and n times.

# Time: O(log n)
# Space: O(1)

nums = [3,4,5,1,2]
l, r = 0, len(nums) - 1
res = nums[0]
while l <= r:
    if nums[l] < nums[r]:
        res = min(res, nums[l])
        break
    m = (l+r) // 2
    res = min(res, nums[m])
    if nums[m] >= nums[l]:
        l = m + 1
    else:
        r = m - 1
print(res)
