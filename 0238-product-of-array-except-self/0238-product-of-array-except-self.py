class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,3,4]
        #[1,1,2,6]
        #[24,12,4,1]
        
        answer = [1] * len(nums)
        
        cur_prod = 1
        for i, num in enumerate(nums):
            answer[i] = cur_prod
            cur_prod *= num
        cur_prod = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= cur_prod 
            cur_prod *= nums[i]
        
        
        
        return answer