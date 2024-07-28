class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # [3,1,2,4]
        
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums