class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda i:i[0])
        
        prevEnd = intervals[0][1]
        overlaps = 0
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                overlaps += 1
                prevEnd = min(end, prevEnd)
        return overlaps
        