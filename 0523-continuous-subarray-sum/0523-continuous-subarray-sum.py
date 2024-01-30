class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remMap = {0:-1}
        runSum = 0
        for R, num in enumerate(nums):
            runSum += num
            rem = runSum % k
            if rem in remMap:
                if R - remMap[rem] >= 2:
                    return True
            else:
                remMap[rem] = R
        return False