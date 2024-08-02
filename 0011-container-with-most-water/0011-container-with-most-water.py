class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = float('-inf')
        while l < r:
            area = (r-l) * min(height[l], height[r])
            maxArea = max(maxArea, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
# Time: O(N)
# Space: O(1)
        