class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = []
        
        for start, end in intervals:
            times.append((start, 1))
            times.append((end, -1))
            
        times.sort()
        count = 0
        maxMeetings = float("-inf")
        for time, incrementer in times:
            count += incrementer
            maxMeetings = max(maxMeetings, count)
            
        return maxMeetings