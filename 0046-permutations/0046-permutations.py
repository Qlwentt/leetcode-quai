class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = []

        def backtrack(curPerm):
            if len(curPerm) == len(nums):
                perms.append(curPerm.copy())
                return
            
            for i in range(len(nums)):
                if not nums[i] in curPerm:
                    curPerm.append(nums[i])
                    backtrack(curPerm)
                    curPerm.pop()
                
        backtrack([])
        return perms
    
    # Time: O(N!*N)
    # Space: O(N)