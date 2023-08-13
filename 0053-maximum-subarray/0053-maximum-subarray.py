class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        prevSum = 0
        
        for num in nums:
            curSum = prevSum + num
            maxSum = max(maxSum, curSum)
            prevSum = max(0, curSum)
        return maxSum
            
        