class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       # [0,1,0,3,12]
      #  P
      #    Q
        P = 0
        for Q in range(len(nums)):
            if nums[Q] != 0:
                nums[P],nums[Q] = nums[Q], nums[P]
                P += 1
        
        