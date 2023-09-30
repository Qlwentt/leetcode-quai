class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combs = []

        def backtrack(i, curComb, curSum):
            if curSum == target:
                combs.append(curComb.copy())
                return
            if i >= len(candidates) or curSum > target:
                return
            
            # include number between 1 and unlimited times
            curComb.append(candidates[i])
            curSum += candidates[i]
            backtrack(i, curComb, curSum)
               
            curComb.pop()
            curSum -= candidates[i]
            # don't include number
            backtrack(i+1, curComb, curSum)
                
        backtrack(0, [], 0)
        return combs