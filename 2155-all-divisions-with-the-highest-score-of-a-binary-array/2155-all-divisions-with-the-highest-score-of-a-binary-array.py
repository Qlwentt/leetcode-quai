class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        prefix = [0] * (len(nums) + 1)
        # [0,0,1,0]
        # [0,1,2,2,3] left
        # [1,1,1,0,0] right
        
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num == 0
            prefix[i+1] = cur_sum

        cur_sum = 0
        for i in range(len(nums)-1,-1,-1):
            cur_sum += nums[i]
            prefix[i] += cur_sum

        max_score = 0
        answer = []
        for i, pre in enumerate(prefix):
            if pre > max_score:
                max_score = pre
                answer = [i]
            elif pre == max_score:
                answer.append(i)
                        
        return answer
        
       