class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    
        perms = []
        nums.sort()

        def backtrack(i, curPerm, curNums):
            if len(curPerm) == len(nums):
                perms.append(curPerm.copy())
                return
                        
            for j in range(len(curNums)):
                next_ = curNums[j+1] if j < len(curNums) - 1 else float('inf')
                if curNums[j] != next_:
                    curPerm.append(curNums[j])
                    backtrack(j+1, curPerm, curNums[:j] + curNums[j+1:])
                    curPerm.pop()
                    
        backtrack(0, [], nums)
        return perms
            
                
            