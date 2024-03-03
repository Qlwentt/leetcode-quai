class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordDict = set(wordDict)
    
        def backtrack(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for j in range(i, len(s)):
                curPart = s[i:j+1]
                if curPart in wordDict:
                    if backtrack(j+1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return backtrack(0)
            
                    
                    
                        