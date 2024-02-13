class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        
        while L <= R:
            mid = (L + R) // 2
            1,2,3,1
            if mid + 1 < len(nums) and nums[mid+1] > nums[mid]:
                # search to the right
                L = mid + 1
            elif mid - 1 >= 0 and nums[mid-1] > nums[mid]:
                # search to the left
                R = mid - 1
            else:
                return mid
        
        
        