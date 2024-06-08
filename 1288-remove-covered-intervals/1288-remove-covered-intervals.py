class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        answer = len(intervals)
        prev = intervals[0]
        for start, end in intervals[1:]:
            prevStart, prevEnd = prev
            if start >= prevStart and end <= prevEnd:
                answer -= 1
            else:
                prev = [start,end]
        return answer