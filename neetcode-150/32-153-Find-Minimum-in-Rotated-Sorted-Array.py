from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        if len(nums) == 1: # only one element
            return nums[0]
        
        if nums[l] < nums[r]: # not rotated
            return nums[l]
        
                      # 0 1 2 3 4 5 6
        while l <= r: #[11,13,15,17]            
            mid = l + (r - l) // 2
            
            # is pivot
            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            
            if nums[l] <= nums[mid]:
                l = mid  + 1
            else:
                r = mid - 1

# O(log(n)) time
# O(1) space