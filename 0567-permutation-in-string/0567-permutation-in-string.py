class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counterS1 = {char:0 for char in "abcdefghijklmnopqrstuvwxyz"}
        for char in s1:
            counterS1[char] += 1
            
        counterS2 = {char:0 for char in "abcdefghijklmnopqrstuvwxyz"}

        L = 0
        R = len(s1) - 1
        
        matches = 0
        for char in s2[L:R+1]:
            counterS2[char] += 1
        for char, count in counterS1.items():
            if counterS2[char] == counterS1[char]:
                matches += 1
        
        while R < len(s2) - 1:                
            if matches == 26:
                return True
                        
            prevChar = s2[L]
            nextChar = s2[R+1]
            
            counterS2[prevChar] -= 1
            if counterS1[prevChar] == counterS2[prevChar]: 
                matches += 1
            elif counterS1[prevChar] == counterS2[prevChar] + 1:
                matches -= 1
            
            counterS2[nextChar] += 1
            if counterS1[nextChar] == counterS2[nextChar]:
                matches += 1
            elif counterS1[nextChar] == counterS2[nextChar] - 1:
                matches -= 1
                
            L += 1
            R += 1
        return matches == 26