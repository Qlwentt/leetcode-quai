class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        result = []
        def backtrack(i):
            if i >= len(nums):
                result.append(subset[:])
                return
            
            # add to subset
            subset.append(nums[i])
            backtrack(i+1)
            
            # didn't add to subset
            subset.pop()
            backtrack(i+1)
        backtrack(0)
        return result