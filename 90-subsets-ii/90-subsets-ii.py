class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        subset = []
        def dfs(i):
            if i == len(nums):
                result.append(subset[::])
                return
            # add the number
            subset.append(nums[i])
            dfs(i+1)
    
            subset.pop()
            while  i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        dfs(0)
        return result