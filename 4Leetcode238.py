# Product of array except self

# Time: O(n)
# Space: O(1)


nums = [1,2,3,4]

def arrayProduct(nums):
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i] 
    postfix =  1
    for i in range(len(nums)-1, -1, -1):
        print(nums[i])
        res[i] *= postfix
        postfix *= nums[i]
    return res

print(arrayProduct(nums))