class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # [0,1,25] [0,0]    
    
        #print((0 - 25) % 26)
        
        p2 = 0
        for p1 in range(len(str1)):
            char1 = str1[p1]
            char2 = str2[p2]
            diff = (ord(char2)-ord(char1)) % 26
            if diff <= 1:
                p2 += 1
            if p2 == len(str2):
                break
        return p2 == len(str2)
            
        