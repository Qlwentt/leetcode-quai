class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [3,5,2,1,6,4]
        #  3,5,1,6,2,4
            
        for i in range(len(nums)-1):
            if i % 2: # odd
                if nums[i+1] > nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else: # even
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        
                