from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding window - fixed size
        "cbaebabacd"
       #  L
       #   R
        
        L = 0
        R = 0
        
        sCount = {char:0 for char in "abcdefghijklmnopqrstuvwxyz"}
        pCount = {char:0 for char in "abcdefghijklmnopqrstuvwxyz"}
        
        for char in p:
            pCount[char] += 1
        
        answer = []
        while R < len(s):
            sCount[s[R]] += 1
            
            if sCount == pCount:
                answer.append(L)
            
            if R-L+1 >= len(p):
                sCount[s[L]] -= 1
                L += 1
            
            R += 1
        return answer
         
        
    
    # O(n) * O(26) (26 letters of alphabet) time
    # O(26) space