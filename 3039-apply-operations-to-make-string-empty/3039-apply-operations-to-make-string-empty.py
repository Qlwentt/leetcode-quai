class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        
        counts = collections.Counter(s)
        max_ = max(counts.values())
        answer = []
        for char in s[::-1]:
            if counts[char] == max_:
                answer.append(char)
                counts[char] = 0
        return "".join(answer[::-1])
                