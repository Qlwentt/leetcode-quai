from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonCharCount = {char:0 for char in "balloon"}
        balloonCounter = Counter("balloon")
        for char in text:
            if char in balloonCounter:
                balloonCharCount[char] += 1
        
              
        adjustedCounts = [count//balloonCounter[char] for char, count in balloonCharCount.items()]
        return min(adjustedCounts)
