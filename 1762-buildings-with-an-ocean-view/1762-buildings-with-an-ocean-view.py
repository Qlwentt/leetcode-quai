class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = float('-inf')
        answer = []
        for i, height in reversed(list(enumerate(heights))):
            if height > maxHeight:
                answer.append(i)
            maxHeight = max(height, maxHeight)
        
        answer.reverse()
        return answer