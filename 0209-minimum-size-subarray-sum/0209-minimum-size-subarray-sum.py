class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        curSum = 0
        L = 0
        R = 0
        
        while R < len(nums):
            curSum += nums[R]      
            while curSum >= target:
                minLen = min(minLen, R - L + 1)
                curSum -= nums[L]
                L += 1
            R += 1
            
        return minLen if minLen != float('inf') else 0