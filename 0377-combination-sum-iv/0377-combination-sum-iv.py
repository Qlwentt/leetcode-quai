class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(cur_sum):
            if cur_sum > target:
                return 0
            if cur_sum == target:
                return 1
    
            answer = 0
            for i in range(len(nums)):
                answer += dp(nums[i]+ cur_sum)
            return answer
        
        return dp(0)
        
      