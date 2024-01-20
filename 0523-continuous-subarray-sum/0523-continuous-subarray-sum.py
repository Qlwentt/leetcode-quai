class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remMap = {0:-1} 
        prefix = 0
        for R, num in enumerate(nums):
            prefix += num
            rem = prefix % k
            if rem in remMap:
                if R - remMap[rem] >= 2:
                    return True
                else:
                    continue
            remMap[rem] = R
            
        return False