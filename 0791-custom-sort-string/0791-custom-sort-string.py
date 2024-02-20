from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count =  Counter(s)
        
        answer = []
        
        for char in order:
            answer.append(count[char] * char)
            del count[char]
            
        for char in count:
            answer.append(count[char]*char)
        
        return "".join(answer)