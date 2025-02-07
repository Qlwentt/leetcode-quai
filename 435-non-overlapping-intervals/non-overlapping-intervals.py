class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        prevEnd = intervals[0][1]
        answer = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # overlap
            if start < prevEnd:
                prevEnd = min(end, prevEnd)
                answer += 1
            else:
                prevEnd = end
        return answer