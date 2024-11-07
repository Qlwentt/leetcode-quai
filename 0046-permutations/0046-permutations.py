class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = []

        def backtrack(curPerm, curNums):
            if len(curPerm) == len(nums):
                perms.append(curPerm.copy())
                return
            
            for i in range(len(curNums)):
                curPerm.append(curNums[i])
                backtrack(curPerm, curNums[:i] + curNums[i+1:])
                curPerm.pop()
                
        backtrack([], nums)
        return perms
    
    # Time: O(N!*N)
    # Space: O(N)