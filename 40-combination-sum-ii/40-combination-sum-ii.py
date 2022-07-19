class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtrack(i, combo, total):
            if total == target:
                result.append(combo[:])
                return
            if i >= len(candidates) or total > target:
                return
            combo.append(candidates[i])
            backtrack(i+1, combo, total + candidates[i])
            combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, combo, total)
            
        backtrack(0,[],0)
        return result
    
    