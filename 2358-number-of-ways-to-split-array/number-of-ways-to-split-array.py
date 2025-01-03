class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
#         cur_sum = 0
#         forward_sums = []
#         for num in nums:
#             cur_sum += num
#             forward_sums.append(cur_sum)
        
#         back_sums = [0] * len(nums)
#         cur_sum = 0
#         for i in range(len(nums)-1,-1,-1):
#             num = nums[i]
#             cur_sum += num
#             back_sums[i] = cur_sum
            
#         answer = 0
#         for a,b in zip(forward_sums,back_sums[1:]):
#             if a >= b:
#                 answer += 1
#         return answer
        right = sum(nums)
        left = 0
        
        n = len(nums)
        answer = 0
        for i, num in enumerate(nums):
            left += num
            right -= num
            
            if i != n - 1 and left >= right:
                answer += 1
                
        return answer