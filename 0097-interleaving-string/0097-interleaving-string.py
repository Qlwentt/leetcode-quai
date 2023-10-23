class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def dfs(i1,i2,i3):
            if i1 >= len(s1) and i2 >= len(s2):
                return i3 >= len(s3)
            
            if (i1,i2,i3) in memo:
                return memo[(i1,i2,i3)]
            
            incI1 = False
            if i1 < len(s1) and i3 < len(s3) and s3[i3] == s1[i1]:
                incI1 = dfs(i1+1,i2,i3+1)
            
            incI2 = False
            if i2 < len(s2) and i3 < len(s3) and s3[i3] == s2[i2]:
                incI2 = dfs(i1,i2+1,i3+1)
            
            memo[(i1,i2,i3)] = incI1 or incI2
            return memo[(i1,i2,i3)]
        
        return dfs(0,0,0)
    
            
               
            
            
            