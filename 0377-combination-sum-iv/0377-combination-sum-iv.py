class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, cur_sum):
            if cur_sum > target:
                return 0
            if cur_sum == target:
                return 1
            if i >= len(nums):
                return 0
            answer = 0
            for j in range(len(nums)):
                answer += dp(j, nums[j]+ cur_sum)
            return answer
        
        return dp(0,0)
        
      