from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        maxLs = [0] * len(height)
        maxRs = [0] * len(height)
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        # [0,0,1,1,2,2,2,2,3,3,3,3]
        for i in range(len(height)):
            prevMax = maxLs[i - 1] if i > 0 else 0
            prevNum = height[i - 1] if i > 0 else 0
            maxL = max(prevMax, prevNum)
            maxLs[i] = maxL
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        # [3,3,3,3,3,3,3,2,2,2,1,0]
        for i in range(len(height)-1, -1, -1):
            prevMax = maxRs[i + 1] if i < len(height) - 1 else 0
            prevNum = height[i + 1] if i < len(height) - 1 else 0
            maxR = max(prevMax, prevNum)
            maxRs[i] = maxR
        
        area = 0
        for i,currHeight in enumerate(height):
            minHeight = min(maxLs[i], maxRs[i])
            water = minHeight - currHeight
            if water < 0:
                water = 0
            area += water
            
        return area
# O(n) time
# O(n) space

# alternative solution in constant space
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         l = 0
#         r = len(height) -1
        
#         rMax = height[r]
#         lMax = height[l]
#         area = 0
#         while r > l:
#             smallest = min(rMax,lMax)
#             if smallest == lMax:
#                 l += 1
#                 water = smallest - height[l]
#                 if water < 0:
#                     water = 0
#                 area += water
#                 lMax = max(height[l], lMax)
#             else:
#                 r -= 1
#                 water = smallest - height[r]
#                 if water < 0:
#                     water = 0
#                 area += water
#                 rMax = max(height[r], rMax)
#         return area
# O(n) time
# O(1) space
            
        