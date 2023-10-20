class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # memoization
        wordDict = set(wordDict)
        memo = {}
        def backtrack(i):
            if i >= len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            for j in range(i, len(s)):
                curPart = s[i:j+1]
                if curPart in wordDict:
                    if backtrack(j+1):
                        memo[i] = True
                        return memo[i]
            memo[i] = False      
            return memo[i]
        return backtrack(0)