from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        
        answer = []
        for char in order:
            if char in counter:
                answer.extend([char]*counter[char])
                counter.pop(char)
                
        for char in counter:
            answer.extend([char]*counter[char])
            
        return "".join(answer)
    
# Time: O(N)
# Space: O(N)