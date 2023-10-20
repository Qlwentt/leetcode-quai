class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = nums[0]
        
        minProd = 1
        maxProd = 1
        for num in nums:            
            minProd, maxProd =  min(num * maxProd, num * minProd, num), max(num * maxProd, num * minProd, num)
            answer = max(maxProd, answer)        
        return answer
    