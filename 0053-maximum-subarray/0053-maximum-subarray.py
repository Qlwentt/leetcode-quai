class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        
        prevSum = 0
        for num in nums:
            prevSum = max(prevSum, 0)
            curSum = prevSum + num
            maxSum = max(curSum, maxSum)
            prevSum = curSum
            
        return maxSum