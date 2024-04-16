class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1
        
        while L<=R:
            mid = (L + R) // 2
            
            if mid + 1 in range(len(nums)) and nums[mid +1] > nums[mid]:
                L = mid + 1
            elif mid -1 in range(len(nums)) and nums[mid-1] > nums[mid]:
                R = mid - 1
            else:
                return mid
        