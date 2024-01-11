from collections import defaultdict
import bisect
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
#         pS = 0
#         pT = 0
        
#         while pS < len(s) and pT < len(t):
#             if s[pS] == t[pT]:
#                 pS += 1
#                 pT += 1
#             else:
#                 pT += 1
        
#         return pS == len(s)

        indexes = defaultdict(list)
        for i, char in enumerate(t):
            indexes[char].append(i)
        
        currMatchI = -1
        for char in s:
            if char not in indexes:
                return False
        
            matchI = bisect.bisect(indexes[char], currMatchI)
            if matchI != len(indexes[char]):
                currMatchI = indexes[char][matchI]
            else:
                return False
        
        return True
            
            
    
        
        
        