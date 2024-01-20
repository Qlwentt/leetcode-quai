from collections import deque
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        #  L
        #    R
        
        sequence = deque([])
        dnaMap = {}
        L = 0
        
        for R in range(len(s)):
            sequence.append(s[R])
            
            if R - L + 1 == 10:
                key = "".join(sequence)
                dnaMap[key] = dnaMap.get(key, 0) + 1
                sequence.popleft()
                L +=1
        return [key for key, value in dnaMap.items() if value > 1]
    
    
        
        