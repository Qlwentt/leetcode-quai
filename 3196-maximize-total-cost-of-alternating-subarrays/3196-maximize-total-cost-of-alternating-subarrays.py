class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        # [1,-2,3,4]
        # [-2,1,3,4] [-1,-2,]
        @cache
        def backtrack(i, isAdd):
            if i == len(nums)-1:
                if isAdd:
                    return nums[i]
                else:
                    return -nums[i]
            # flip next sign
            if isAdd:
                flip = nums[i] + backtrack(i+1, not isAdd)
            else:
                flip = -nums[i] + backtrack(i+1, not isAdd)
            
            # don't flip sign
            dontFlip = float('-inf')
            
            if isAdd:
                dontFlip = nums[i] + backtrack(i+1, isAdd)
                
            return max(flip, dontFlip)
        return backtrack(0, True)
                
            
                    
        