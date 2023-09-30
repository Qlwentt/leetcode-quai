class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        def backtrack(i, curSet):
            if i >= len(nums):
                solution.append(curSet.copy())
                return
            
            # include num in set
            curSet.append(nums[i])
            backtrack(i+1, curSet)

            # don't include num in set
            curSet.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, curSet)
        backtrack(0, [])
        return solution