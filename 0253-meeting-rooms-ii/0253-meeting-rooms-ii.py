class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
      # max number of meetings happening at the same time
        times = []
        
        for start, end in intervals:
            times.append((start, 1))
            times.append((end, -1))
            
        times.sort()
        
        rooms = 0
        maxRooms = 0
        
        for time in times:
            rooms += time[1]
            maxRooms = max(rooms, maxRooms)
            
        return maxRooms
        
        