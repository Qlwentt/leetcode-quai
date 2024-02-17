class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
   # [16,1,0,9,100]
  #     L R
        L = None
        for i in range(len(nums)):
            if nums[i] < 0:
                L = i
            nums[i] = nums[i] ** 2
        
        if L == None:
            return nums
        if L == len(nums) - 1:
            nums.reverse()
            return nums
        R = L + 1
        
        answer = []
        while L >= 0 or R < len(nums):
            numL = nums[L] if L in range(len(nums)) else float('inf')
            numR = nums[R] if R in range(len(nums)) else float('inf')
            if numL < numR:
                answer.append(numL)
                L -= 1 
            else:
                answer.append(numR)
                R += 1
        return answer