class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    
        perms = []
        nums.sort()

        def backtrack(curPerm, curNums):
            if len(curPerm) == len(nums):
                perms.append(curPerm.copy())
                return
                        
            for i in range(len(curNums)):
                next_ = curNums[i+1] if i < len(curNums) - 1 else float('inf')
                if curNums[i] != next_:
                    curPerm.append(curNums[i])
                    backtrack(curPerm, curNums[:i] + curNums[i+1:])
                    curPerm.pop()
                    
        backtrack([], nums)
        return perms
            
                
            