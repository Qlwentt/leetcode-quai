class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(i,combo, total):
            if total == target:
                result.append(combo[:])
                return
            if total > target or i >= len(candidates):
                return
            
            # add the num
            combo.append(candidates[i])
            backtrack(i, combo, candidates[i] + total)
            
            # choose to not add the num
            combo.pop()
            backtrack(i+1, combo, total)
        backtrack(0, [], 0)
        return result