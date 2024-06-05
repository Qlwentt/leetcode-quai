class Solution:
    def partitionString(self, s: str) -> int:
        charSet = set()
        answer = 0
        for char in s:
            if char in charSet:
                charSet = set()
                answer += 1
            charSet.add(char)
                
        return answer + 1