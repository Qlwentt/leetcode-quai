class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        
        answer = []
        def backtrack(i, curWords):
            if i == len(s):
                answer.append(" ".join(curWords))
                return
            
            for j in range(i, len(s)):
                curWord = s[i:j+1]
                if curWord in words:
                    curWords.append(curWord)
                    backtrack(j+1, curWords)
                    curWords.pop()
        backtrack(0, [])
        return answer