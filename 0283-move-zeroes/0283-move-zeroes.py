class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        
        
        
            