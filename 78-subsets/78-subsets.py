class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return          
            
            # decision 1: add nums[i] to subset
            subset.append(nums[i])
            dfs(i+1)
            
            # decision 2: don't add nums[i] to subset
            subset.pop()
            dfs(i+1)
        dfs(0)
        return result