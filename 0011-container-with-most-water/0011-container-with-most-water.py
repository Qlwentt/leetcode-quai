class Solution:
    def maxArea(self, height: List[int]) -> int:
        # pairs = (1,8,1), (1,6,2), (1,2,3), (1,5,4) (1,4,5), (1,8,6), (1,3,7), (1,7,8) possible max: 8
        #         (8,1,1), (8,6,1), (8,2,2),                                    (8,7,7) possible max: 64
        
        # maxArea = 0
        # for i in range(len(height)):
        #     for j in range(len(height)):
        #         if i == j:
        #             continue
        #         width = abs(i-j)
        #         h = min(height[i], height[j])
        #         area = width * h
        #         maxArea = max(area, maxArea)
        # return maxArea
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l < r:
            width = r - l
            h = min(height[r],height[l])
            area = width * h
            maxArea = max(area, maxArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
        
        