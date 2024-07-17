class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        monotone_increasing = True
        monotone_decreasing = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                monotone_increasing = False
                break
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                monotone_decreasing = False
                break
                
        return monotone_increasing or monotone_decreasing
                