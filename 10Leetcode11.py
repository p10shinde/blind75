# Container with most water

# Given n non-negative integers a1, a2, ..., an where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of the line i is 
# at (i, ai) and (i, 0). Find two lines, which, together with the x-axis
# forms a container such that the container contains the most water

height = [1,8,6,2,5,4,8,3,7]
# height = [4,3,2,1,4]
# height = [2,1]

# BRUTE FORCE
# Time: O(n2)
maxC = height[0] 
for l in range(len(height)):
    for r in range(l+1, len(height)):
        area = (r - l) * min(height[l], height[r])
        maxC = max(maxC, area)
# print(maxC)

# Optimal
# Time: O(n)
l = 0
r = len(height) - 1
maxArea = 0
while l < r:
    area = (r-l) * min(height[l], height[r])
    if height[l] < height[r]:
        l+=1
    else:
        r-=1

    maxArea = max(area, maxArea)
print(maxArea)