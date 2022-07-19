class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(i, combo, total):
            if total == target:
                result.append(combo[:])
                return
            if i >= len(candidates) or total > target:
                return
            
            # add number
            combo.append(candidates[i])
            backtrack(i, combo, total + candidates[i])
            
            # don't add number
            combo.pop()
            backtrack(i+1, combo, total)
            
        backtrack(0, [], 0)
        return result