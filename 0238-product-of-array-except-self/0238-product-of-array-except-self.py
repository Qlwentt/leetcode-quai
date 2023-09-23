class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightProd = [1] * len(nums)
        leftProd = [1] * len(nums)
        
        [1 ,2 ,3 ,4 ]
        [1 , 1, 2, 6]
        [24, 12, 4, 1]
        [24, 12, 8, 6]
        
        
        for i in range(1,len(nums)):
            leftProd[i] = leftProd[i-1] * nums[i-1]
    
        for i in range(len(nums) -2, -1, -1):
            rightProd[i] = rightProd[i+1] * nums[i+1]
        answer = []  
        for i in range(len(nums)):
            answer.append(leftProd[i]* rightProd[i])
        return answer