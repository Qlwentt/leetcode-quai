class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        #  3 3 3 3 3 3 3 3 2 2 2 1
        #  0 1 1 2 2 2 2 3 3 3 3 3
        forward_maxes = [0] * len(height)
        backward_maxes = [0] * len(height)
        
        max_ = float('-inf')
        for i, h in enumerate(height):
            max_ = max(h, max_)
            forward_maxes[i] = max_
        max_ = float('-inf')
        for i in range(len(height)-1,-1,-1):
            max_ = max(height[i], max_)
            backward_maxes[i] = max_
        area = 0
        for i, h in enumerate(height):
            area += max(min(forward_maxes[i], backward_maxes[i])-h,0)
        
        return area
        
            