from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #  0 1 2 3 4 5 6 7 8
        # [1,8,6,2,5,4,8,3,7]
        #  x               x   shortest = min(height[p1], height[p2]) = 1
        #                      area = shortest * (p2 - p1) = 1 * (8 - 0) = 8
        #                      maxArea = max(maxArea,area) = 8
        # [1,10,6,2,5,4,10,3,7]
        
        l = 0
        r = len(height) - 1
        maxArea = 0
        while r > l:
            heightL = height[l]
            heightR = height[r]
            
            shortest = min(heightL, heightR)
            area = shortest * (r - l)
            maxArea = max(area,maxArea)
            
            if shortest == heightL:
                l += 1
            else:
                r -= 1
        return maxArea

# O(n) time
# O(1) space