class Solution:
    def numDecodings(self, s: str) -> int:
        numMap = {str(num+1): letter for num, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        memo = {}
        def backtrack(i):
            if i > len(s):
                return 0
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]
            
            res = 0
            # take only one num
            nextNum = s[i]
            if nextNum in numMap:
                res += backtrack(i+1)
            
            # take two nums
            nextNum = s[i:i+2]
            if nextNum in numMap:
                res += backtrack(i+2)

            memo[i] = res    
            return res
                
        return backtrack(0)
            
        