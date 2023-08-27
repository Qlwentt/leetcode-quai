class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        [-2,1,-3,4,-1,2,1,-5,4]
        maxSum = float('-inf')
        
        sum_ = 0
        for num in nums:
            sum_ += num
            maxSum = max(sum_, maxSum)
            sum_ = max(sum_, 0)
        return maxSum
            
        