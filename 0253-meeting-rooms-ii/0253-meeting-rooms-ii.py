class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = []
        
        for start, end in intervals:
            times.append([start, 1])
            times.append([end, -1])
            
        times.sort()
        rooms = 0
        maxRooms = 0
        for time, incr in times:
            rooms += incr
            maxRooms = max(rooms, maxRooms)
                    
        return maxRooms
        