class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1 = text1
        s2 = text2
#         memo = {}
#         def dfs(i1,i2):
#             if i1 == len(s1) or i2 == len(s2):
#                 return 0
            
#             if (i1, i2) in memo:
#                 return memo[(i1,i2)]
            
#             if s1[i1] == s2[i2]:
#                 ans = 1 + dfs(i1+1, i2+1)
#                 memo[(i1,i2)] = ans
#                 return ans
#             inc1 = dfs(i1+1, i2)
#             inc2 = dfs(i1, i2+1)
#             ans = max(inc1, inc2)
#             memo[(i1,i2)] = ans
#             return ans
#         return dfs(0,0)
        dp = collections.defaultdict(int) # initalize out of bounds to zeros
        n = len(s1)
        m = len(s2)
        
        for i1 in range(n-1,-1,-1):
            for i2 in range(m-1,-1,-1):
                if s1[i1] == s2[i2]:
                    dp[(i1,i2)] = 1 + dp[(i1+1,i2+1)]
                else:
                    inc1 = dp[(i1+1, i2)]
                    inc2 = dp[(i1, i2+1)]
                    dp[(i1,i2)] = max(inc1, inc2)
        return dp[(0,0)]
        
            
        
        
        