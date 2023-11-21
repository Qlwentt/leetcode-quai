class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        prevMax = float("-inf")
        answer = []
        for i in range(len(heights)-1, -1, -1):
            if prevMax < heights[i]:
                answer.append(i)
            prevMax = max(heights[i], prevMax)
        answer.reverse()
        return answer