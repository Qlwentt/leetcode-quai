class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(i,curr, total):
            if total == target:
                result.append(curr.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            # add the current number
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            
            curr.pop()
            dfs(i+1, curr, total)
            
        dfs(0, [], 0)
        return result