from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        right = Counter(s)
        pals = set()
        
        for midChar in s:
            right[midChar] -= 1
            if right[midChar] == 0:
                del right[midChar]
            
            for outsideChar in "abcdefghijklmnopqrstuvwxyz":
                if outsideChar in left and outsideChar in right:
                    pals.add(outsideChar + midChar + outsideChar)
            
            left.add(midChar)
                
        return len(pals)