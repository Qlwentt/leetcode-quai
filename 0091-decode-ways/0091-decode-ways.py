class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def backtrack(i):
            if i >= len(s):
                return 1
            count  = 0
            for j in range(i,len(s)):
                substring = s[i:j+1]
                if substring[0] != "0" and int(substring) in range(1,27):
                    count += backtrack(j+1)
            
            return count
            
        return backtrack(0)  
             
        