class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
       # really asking -- are there overlaps
        intervals.sort(key=lambda pair: pair[0])
        
        if not intervals:
            return True
        
        for i in range(1, len(intervals)):
            prevStart, prevEnd = intervals[i-1]
            start, end = intervals[i]
            
            if start < prevEnd:
                return False
        return True