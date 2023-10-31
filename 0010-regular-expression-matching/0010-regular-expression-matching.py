class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(iP,iS):
            if iP >= len(p) and iS >= len(s):
                return True
            
            if iP >= len(p):
                return False
            
            if (iP, iS) in memo:
                return memo[(iP, iS)]
            
            match = iS < len(s) and (p[iP] == s[iS] or  p[iP] == ".") 
            if iP + 1 < len(p) and p[iP+1] == "*":
                # choose to use the character 1 or unlimited times
                use = match and dfs(iP, iS+1)
                # choose to skip the character
                skip = dfs(iP+2, iS)
                
                memo[(iP,iS)] = skip or use
                return memo[(iP,iS)]
            if match:
                memo[(iP,iS)] = dfs(iP+1, iS+1)
                return memo[(iP,iS)]
            memo[(iP,iS)] = False
            return memo[(iP,iS)]
            
        
        return dfs(0,0)
                