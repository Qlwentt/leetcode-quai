from collections import deque, defaultdict
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        dayCanPerform = defaultdict(lambda: 1) # 1: 9, 2: 10
      #  [1,2,1,2,3,1]
        
        day = 0 # 1 2 5 6 7 8 9
        for taskId in tasks:
            day += 1
            day = dayCanPerform[taskId] if day < dayCanPerform[taskId] else day
            dayCanPerform[taskId] = day + (space + 1)
        return day