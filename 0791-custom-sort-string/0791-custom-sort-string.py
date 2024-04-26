from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        
        answer = []
        for char in order:
            
            if char in counter:
                answer.append(char * counter[char])
                del counter[char]
        
        for char in counter:
            answer.append(char * counter[char])
            
        return "".join(answer)
        