class Solution:
    #memoization
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        nums = [1] + nums + [1]
        def dfs(L,R):
            if L > R:
                return 0
            
            if (L,R) in memo:
                return memo[(L,R)]
            
            maxCoins = 0
            for i in range(L,R+1):
                # make this the last element to get popped
                coins = nums[L-1] * nums[i] * nums[R+1]
                maxCoins = max((coins + dfs(L,i-1) + dfs(i+1,R)), maxCoins)
                memo[(L,R)] = maxCoins
            return memo[(L,R)]       
        
        return dfs(1, len(nums) - 2)


