class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        numDict = {i+1:1 for i in range(n)}
        numDict[n] = 2
        
        for num in nums:
            if num in numDict:
                numDict[num] -= 1
                if numDict[num] == 0:
                    del numDict[num]
            else:
                return False
            
        return len(numDict) == 0
        