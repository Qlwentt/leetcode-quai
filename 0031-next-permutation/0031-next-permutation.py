class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find first number that is decreasing from right to left
        def reverse(L,R):
            while L < R:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
                R -= 1
            
        pivot = None
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                pivot = i - 1
                break
        
        if pivot == None:
            nums.reverse()
            return
        # find first number that is greater than pivot from right to left, swap
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                # reverse remaining
                reverse(pivot+1, len(nums)-1)
                return
        
        
        
        
        