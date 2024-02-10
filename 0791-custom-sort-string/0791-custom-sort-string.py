from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        answer = []
        
        for char in order:
            answer.extend([char]* count[char])
            del count[char]
        
        for char in count:
            answer.extend([char] * count[char])
            
        return "".join(answer)