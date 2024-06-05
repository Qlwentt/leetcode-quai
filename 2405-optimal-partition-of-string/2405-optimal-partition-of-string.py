class Solution:
    def partitionString(self, s: str) -> int:
        # "abacaba"
        #    R
        charSet = set()
        answer = 0
        for char in s:
            if char in charSet:
                charSet = set()
                answer += 1
            
            
            charSet.add(char)
                
        answer += 1
        return answer