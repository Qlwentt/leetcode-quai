class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        candidates.sort()
        def backtrack(i, curComb, curSum):
            if curSum == target:
                combs.append(curComb.copy())
                return
            
            if curSum > target or i >= len(candidates):
                return
            
            # between 1 - multiple nums
            curComb.append(candidates[i])
            curSum += candidates[i]
            backtrack(i+1, curComb, curSum)
            
            # skip num
            curComb.pop()
            curSum -= candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i+1, curComb, curSum)
        backtrack(0, [], 0)
        return combs