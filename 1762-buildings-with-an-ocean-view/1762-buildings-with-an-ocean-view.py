from collections import deque
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxSeen = float("-inf") # 3
        answer = deque([])
     #
        for i, height in reversed(list(enumerate(heights))):
            if height > maxSeen:
                answer.appendleft(i)
            maxSeen = max(height, maxSeen)
        
        return answer
        