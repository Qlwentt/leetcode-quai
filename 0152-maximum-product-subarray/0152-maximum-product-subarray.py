class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = float('-inf')
        
        min_prod = 1
        max_prod = 1
        
        for num in nums:
                                       
            min_prod, max_prod = min(min_prod*num, max_prod*num, num), max(min_prod*num, max_prod*num, num)
            answer = max(max_prod, answer)
        
        return answer