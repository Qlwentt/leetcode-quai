class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        prev = '0'
        for char in target:
            if char != prev:
                flips += 1
            prev = char
        
        return flips
        