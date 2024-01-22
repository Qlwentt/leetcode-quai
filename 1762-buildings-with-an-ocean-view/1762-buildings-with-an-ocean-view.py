from collections import deque
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = float('-inf')
        answer = deque([])
        for i in range(len(heights)-1,-1,-1):
            cur = heights[i]
            if cur > maxHeight:
                answer.appendleft(i)
            maxHeight = max(cur, maxHeight)
            
        return answer
    
    # Time: O(N)
    # Space: O(N) if you count answer, O(1) if you don't count answer