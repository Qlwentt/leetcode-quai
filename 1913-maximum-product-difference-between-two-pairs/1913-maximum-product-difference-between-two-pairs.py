class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1 = min(nums)
        nums.pop(nums.index(min1))
        max1 = max(nums)
        nums.pop(nums.index(max1))
        
        min2 = min(nums)
        nums.pop(nums.index(min2))
        max2 = max(nums)
        
        return (max1 * max2) - (min1 * min2)
        
        
            