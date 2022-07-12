class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        mins = [min(x,y) for x,y in rectangles]
        maxLen = max(mins)
        return mins.count(maxLen)