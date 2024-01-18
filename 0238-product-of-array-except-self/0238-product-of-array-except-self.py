class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightProd = [1] * len(nums)
        leftProd = [1] * len(nums)
        
#         [1,2,3,4]
        
#         [1, 1, 2,6]
#         [24,12,4,1]
        
        for i in range(1,len(nums)):
            leftProd[i] = nums[i-1] * leftProd[i-1]
                        
        for i in range(len(nums)-2,-1,-1):
            rightProd[i] = nums[i+1] * rightProd[i+1]
        
        # [24,12,8,6]
        answer = [1] * len(nums)
        for i in range(len(nums)):
            answer[i] = leftProd[i] * rightProd[i]
        
        return answer
        