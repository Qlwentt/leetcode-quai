class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = float('-inf')
        answer = []
        for i in range(len(heights)-1,-1,-1):
            cur = heights[i]
            if cur > maxHeight:
                answer.append(i)
            maxHeight = max(cur, maxHeight)
            
        answer.reverse()
        return answer