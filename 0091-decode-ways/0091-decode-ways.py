class Solution:
    def numDecodings(self, s: str) -> int:
        numMap = {str(num+1): letter for num, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        memo = {}
        def backtrack(i):
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]
            res = 0
            for j in range(i, len(s)):
                curPart = s[i:j+1]
                if curPart in numMap:
                    res += backtrack(j+1)
            memo[i] = res    
            return res
                
        return backtrack(0)
            
        