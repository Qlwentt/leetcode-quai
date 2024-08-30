class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        #  0 1 1 2 2 2 2 3 3 3 3 3
        #  3 3 3 3 3 3 3 3 2 2 2 1
        left_maxes = [0] * len(height)
        right_maxes = [0] * len(height)
        
        cur_max = float('-inf')
        for i, h in enumerate(height):
            cur_max = max(h, cur_max)
            left_maxes[i] = cur_max
        
        cur_max = float('-inf')
        for i in range(len(height)-1,-1,-1):
            cur_max = max(height[i], cur_max)
            right_maxes[i] = cur_max
        
        area = 0
        for i, h in enumerate(height):
            area += max(min(left_maxes[i], right_maxes[i])-h,0)
        
        return area
        
            