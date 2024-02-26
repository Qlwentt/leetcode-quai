class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(L,R):
            while L < R:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
                R -= 1
        
        pivot = None
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        
        if pivot == None:
            nums.reverse()
            return
        
        for i in range(len(nums)-1,pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                reverse(pivot+1, len(nums)-1)
                break
                