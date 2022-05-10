# Check if contains duplicate
nums = [1,2,3,1]
nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]
# Time: O(nlogn)
# Space: O(1) 
def checkIfDuplicate_using_sort(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# Time: O(n)
# Space: O(n) 
def checkIfDuplicate_using_hashmap(nums):
    hm = set()
    for i in range(len(nums)):
        if nums[i] in hm: return True
        else: hm.add(nums[i])
    return False
    
# print(checkIfDuplicate_using_sort(nums))
print(checkIfDuplicate_using_hashmap(nums))