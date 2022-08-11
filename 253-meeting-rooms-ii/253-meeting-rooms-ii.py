class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start = [i for i, j in intervals]
        end = [j for i, j in intervals]
        
        start.sort()
        end.sort()
        
        p1 = 0
        p2 = 0
        simultMeetings = 0
        maxMeetings = 0
        while p1 < len(start):
            if start[p1] < end[p2]:
                simultMeetings += 1
                p1 += 1
            else:
                simultMeetings -= 1
                p2 += 1
            maxMeetings = max(simultMeetings, maxMeetings)
        
        return maxMeetings
            
        