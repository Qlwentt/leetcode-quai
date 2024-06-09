class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
    
        
        n = len(nums)
        def get_pivot(nums):
            pivot = None
            for i in range(len(nums)-1):
                if nums[i+1] < nums[i]:
                    if pivot is None:
                        pivot = i+1
                    else:
                        return -1
            return pivot
                
        pivot = get_pivot(nums)
        if pivot == -1:
            return -1
        if pivot == None:
            return 0
        
        return n-pivot if get_pivot(nums[pivot:]+nums[:pivot]) == None else -1
                
        
            