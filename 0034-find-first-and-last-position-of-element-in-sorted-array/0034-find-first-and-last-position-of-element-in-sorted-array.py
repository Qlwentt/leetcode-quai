class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        
        ansL =  l if l < len(nums) and nums[l] == target else -1
        
        if ansL == -1:
            return [-1,-1]
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        
        return [ansL, r]
    
# Time: O(log(N))
# Space: O(1)
        