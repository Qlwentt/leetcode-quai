class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        powerSet = []
        nums.sort()

        def backtrack(i, curSet):
            if i >= len(nums):
                powerSet.append(curSet.copy())
                return
            
            # include between 1 and multiple of the number
            curSet.append(nums[i])
            backtrack(i+1, curSet)
            
            # do not include the number
            curSet.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, curSet)
        
        backtrack(0, [])
        return powerSet