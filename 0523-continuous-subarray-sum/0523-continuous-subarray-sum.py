class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        numsDict = {0: -1}
        
        curSum = 0
        for i, num in enumerate(nums):
            curSum += num
            rem = curSum % k
            if rem in numsDict and i - numsDict[rem] >= 2:
                return True
            elif rem not in numsDict:
                numsDict[rem] = i
        return False
            
    
            
        
        
            