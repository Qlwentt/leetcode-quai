class Solution:
    
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i1,i2):
            if i1 >= len(s) and i2 >= len(t):
                return 1
            
            if i1 >= len(s):
                return 0
            
            if i2 >= len(t):
                return 1
            
            if (i1, i2) in memo:
                return memo[(i1,i2)]
            
            if s[i1] == t[i2]:
                incBoth = dfs(i1+1, i2+1)
                incI1 = dfs(i1+1, i2)
                memo[(i1,i2)] = incBoth + incI1
                return memo[(i1,i2)]
            else:
                memo[(i1,i2)] = dfs(i1+1, i2)
                return memo[(i1,i2)]
            
        return dfs(0,0)