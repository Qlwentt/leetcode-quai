class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int: 
        if k <= 1:
            return 0
        
        cur_product = 1
        L = 0
        answer = 0
        for R in range(len(nums)):
            cur_product *= nums[R]
            while cur_product >= k:
                cur_product //= nums[L]
                L += 1
            answer += R-L+1
        return answer
        