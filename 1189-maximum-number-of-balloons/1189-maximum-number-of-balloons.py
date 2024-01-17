class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonMap = {char: 0 for char in "balloon"}
        
        for char in text:
            if char in balloonMap:
                balloonMap[char] += 1
        
        balloonMap["o"] =  balloonMap["o"] // 2
        balloonMap["l"] =  balloonMap["l"] // 2
        
        return min(balloonMap.values())