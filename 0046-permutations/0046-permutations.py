class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = []
        
        def backtrack(i, curPerm, curNums):
            if len(curPerm) == len(nums):
                perms.append(curPerm.copy())
                return
            
            for j in range(len(curNums)):
                curPerm.append(curNums[j])
                backtrack(j+1, curPerm, curNums[:j] + curNums[j+1:])
                curPerm.pop()

        backtrack(0, [], nums)
        return perms