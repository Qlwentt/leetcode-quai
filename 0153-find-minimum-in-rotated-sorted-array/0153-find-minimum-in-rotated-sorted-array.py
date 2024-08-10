class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] <= nums[-1]:
            return nums[0]
        # [4,5,1,2,3]
        #    R
        #  M L
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            
            if mid + 1 < len(nums) and nums[mid + 1] < nums[mid]:
                return nums[mid+1]
            elif nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
                