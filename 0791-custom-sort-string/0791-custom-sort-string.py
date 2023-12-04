from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        countS = Counter(s)
        
        answer = []
        
        for char in order:
            answer.extend([char]*(countS[char]))
            countS[char] = 0
    
        for char in countS:
            answer.extend([char]*countS[char])
            
        return "".join(answer)