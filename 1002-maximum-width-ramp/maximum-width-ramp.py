class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        prefix_maxes = [0] * len(nums)
        cur_max = 0
        for i in range(len(nums)-1, -1, -1):
            cur_max = max(nums[i], cur_max)
            prefix_maxes[i] = cur_max
        
        l = 0
        # [6,0,8,2,1,5]
        # [8,8,8,5,5,5]
        #  L
        #  R
        ramp = 0
        for r in range(len(nums)):
            while prefix_maxes[r] < nums[l]:
                l += 1
            ramp = max(r-l, ramp)
        return ramp
