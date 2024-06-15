class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        for i in range(1, 101):
            if word * i not in sequence:
                break
        
        return i - 1
                
            
        