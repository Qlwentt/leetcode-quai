class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            while start < end:
                nums[start] , nums[end] = nums[end] , nums[start]
                start += 1
                end -= 1
        
        pivot = None
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        if pivot is not None:
          # find number just larger than pivot
            nextGreater = None
            for j in range(len(nums)-1, pivot, -1):
                if nums[j] > nums[pivot]:
                    nums[j], nums[pivot] = nums[pivot] , nums[j]
                    break
            reverse(pivot+1,len(nums)-1)
        else:
            nums.reverse()
        
        