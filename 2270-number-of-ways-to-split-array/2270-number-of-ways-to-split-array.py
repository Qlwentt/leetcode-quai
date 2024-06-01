class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
#         [10,14,6,7]
#         [13,3,-1,7]
        
#         10 > 3  += 1
#         14 > -1  += 1
#         6 > 7    += 0
        
        cur_sum = 0
        forward_sums = []
        for num in nums:
            cur_sum += num
            forward_sums.append(cur_sum)
        
        back_sums = [0] * len(nums)
        cur_sum = 0
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            cur_sum += num
            back_sums[i] = cur_sum
            
        answer = 0
        for a,b in zip(forward_sums,back_sums[1:]):
            if a >= b:
                answer += 1
        return answer