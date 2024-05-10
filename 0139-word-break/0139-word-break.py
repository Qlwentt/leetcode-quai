class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}
        def backtrack(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            for j in range(i,len(s)):
                curWord = s[i:j+1]
                if curWord in words:
                    if backtrack(j+1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return backtrack(0)
        