from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #(height,index)
        heights.append(0)
        
        for i, height in enumerate(heights):
            topI = i
            while stack and height < stack[-1][0]:
                topHeight, topI = stack.pop()
                area = (i - topI) * topHeight
                maxArea = max(area, maxArea)
            stack.append((height, topI))
            
        return maxArea
# O(n) time
# O(n) space