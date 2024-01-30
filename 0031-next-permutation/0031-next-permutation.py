class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # find first decreasing from end to get pivot
        # [3,2,1,2,3]
        pivot = None
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i - 1
                break
        # if found pivot, swap with number just larger than pivot
        if pivot is not None:
            for i in range(len(nums)-1, pivot, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
            # reverse numbers from pivot + 1 to end
            reverse(pivot+1,len(nums)-1)
        # else reverse all nums
        else:
            nums.reverse()