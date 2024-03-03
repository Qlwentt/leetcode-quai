from collections import defaultdict
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        dayToPerformTask = defaultdict(int)
        day = 0
        for task in tasks:
            day += 1
            day = dayToPerformTask[task] if day < dayToPerformTask[task] else day
            dayToPerformTask[task] = day + space + 1
        
        return day