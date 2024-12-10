class Solution:
    def maximumLength(self, s: str) -> int:
        substrings = collections.defaultdict(int)
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub = s[i:j+1]
                if sub == s[j] * len(sub):
                    substrings[sub] += 1
        answer = -1
        for sub,count in substrings.items():
            if count >= 3:
                answer = max(answer, len(sub))
        
        return answer