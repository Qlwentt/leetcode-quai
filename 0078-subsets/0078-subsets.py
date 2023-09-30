class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = []
        def backtrack(i, curSet):
            if i >= len(nums):
                powerSet.append(curSet.copy())
                return
            
            # include num in set
            curSet.append(nums[i])
            backtrack(i+1, curSet)

            # don't include num in set
            curSet.pop()
            backtrack(i+1, curSet)
            
        backtrack(0, [])
        return powerSet
            
            