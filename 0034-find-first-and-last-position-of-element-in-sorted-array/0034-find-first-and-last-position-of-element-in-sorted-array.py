class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        leftmost = -1
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid] >= target:
                r = mid - 1
                if nums[mid] == target:
                    leftmost = mid
            else:
                l = mid + 1
        
        if leftmost == -1:
            return [-1,-1]
        
        l = 0
        r = len(nums) - 1
        # rightmost = -1
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid] <= target:
                l = mid + 1
                # if nums[mid] == target:
                #     rightmost = mid
            else:
                r = mid - 1
        
        return [leftmost, r]
        # return [leftmost, rightmost]
    
# Time: O(log(N))
# Space: O(1)
        