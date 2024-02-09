from collections import deque
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        answer = deque([])
        maxHeight = float('-inf')
        
        for i, height in reversed(list(enumerate(heights))):
            if height > maxHeight:
                answer.appendleft(i)
            maxHeight = max(maxHeight, height)
        
        return answer