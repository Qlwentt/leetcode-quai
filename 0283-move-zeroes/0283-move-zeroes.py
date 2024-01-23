class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        [1,3,12,0,0]
       #     P
       #         Q
        P = 0
        
        for Q, num in enumerate(nums):
            if num != 0:
                nums[P], nums[Q] = nums[Q], nums[P]
                P += 1
        
        
        
            