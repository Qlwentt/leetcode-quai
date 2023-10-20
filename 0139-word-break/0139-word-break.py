class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # memoization
#         wordDict = set(wordDict)
#         memo = {}
#         def backtrack(i):
#             if i >= len(s):
#                 return True
            
#             if i in memo:
#                 return memo[i]
            
#             for j in range(i, len(s)):
#                 curPart = s[i:j+1]
#                 if curPart in wordDict:
#                     if backtrack(j+1):
#                         memo[i] = True
#                         return memo[i]
#             memo[i] = False      
#             return memo[i]
#         return backtrack(0)
    
        # dp
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        
        for i in range(n-1, -1,-1):
            for j in range(n-1, i-1, -1):
                curPart = s[i:j+1]
                if curPart in wordDict:
                    dp[i] = dp[j+1]
                    if dp[i]:
                        break
        return dp[0]
        
        