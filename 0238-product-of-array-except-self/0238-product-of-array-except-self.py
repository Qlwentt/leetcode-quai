class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    # O(N) space solution
    
        forward = [1] * len(nums)
        backward = [1] * len(nums)
        
        cur_prod = 1
        for i, num in enumerate(nums):
            forward[i] = cur_prod
            cur_prod *= num
        cur_prod = 1
        for i in range(len(nums)-1,-1,-1):
            backward[i] = cur_prod
            cur_prod *= nums[i]
        
        answer = []
        for f, b in zip(forward, backward):
            answer.append(f*b)
        
        return answer
    # Time: O(N)
    # Space: O(N)
        
    # constant space solution
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
    
# Time: O(N)
# Space: O(1) not counting output


            