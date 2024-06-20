class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counts = collections.Counter(power)
        keys = list(sorted(counts))
        N = len(keys)
        next_i = [len(keys)] * len(keys)  
                                          
        p = 0
        q = 0
        while p < len(keys):
            if keys[p] > keys[q] + 2:
                next_i[q] = p
                q += 1
            else:
                p += 1
    
        @cache
        def dp(i):
            if i == len(keys) -1:
                return keys[i] * counts[keys[i]]
            if i == len(keys):
                return 0
            # choose this number and next one available recursively
            choose = dp(next_i[i]) + keys[i] * counts[keys[i]]
            skip = dp(i+1)
            return max(choose, skip)
        return dp(0)
        
        
#         dp = [0] * N
        
#         for i in range(N):
#             dp[i] = 0
#             for j in range(1, 4):
#                 if i - j >= 0 and keys[i] - keys[i - j] > 2:
#                     dp[i] = max(dp[i], dp[i - j])
#             dp[i] += f[keys[i]] * keys[i]
            
#             # dp[i] now contains the best damage using keys[i]
#             if i - 1 >= 0:
#                 dp[i] = max(dp[i], dp[i - 1])
#             # now dp[i] contains the best damage using keys[i] or not using keys[i]
#         return max(dp)


#         def backtrack(i, prev):
#             if i == len(power):
#                 return curSum
#             # choose
#             choose = float('-inf')
#             p = power[i][0]
#             if p > prev + 2:
#                 choose = backtrack(i+1, power[i][1] + curSum, p)
            
#             # skip
#             skip = backtrack(i+1, curSum, prev)
            
#             return max(choose, skip)
        
#         return backtrack(0, 0, float('-inf'))
            
            
            
            