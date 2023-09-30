class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solution = set()
        
        def backtrack(i, curSet):
            if i >= len(nums):
                oneSet = curSet.copy()
                oneSet.sort()
                solution.add(tuple(oneSet))
                return
            
            # include num in set
            curSet.append(nums[i])
            backtrack(i+1, curSet)

            # don't include num in set
            curSet.pop()
            backtrack(i+1, curSet)
        backtrack(0, [])
        return solution