class Solution:
    def validPalindrome(self, s: str) -> bool:    
    
        start = 0
        end = len(s) - 1
        
        while end > start:
            if s[end] != s[start]:
                return self.isPal(s[:start]+ s[start+1:]) or self.isPal(s[:end]+ s[end+1:])
            start += 1
            end -= 1
        return True
    
    
    def isPal(self,s):
        start = 0
        end = len(s) - 1
            
        while end > start:
            s1 = s[start]
            s2 = s[end]
            if s1 != s2:
                return False
            start += 1
            end -= 1
        return True
    