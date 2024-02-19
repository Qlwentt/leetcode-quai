from collections import defaultdict
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        dayCanComplete = defaultdict(int)
        day = 0
        for task in tasks:
            day = day + 1 if day >= dayCanComplete[task] else dayCanComplete[task]
            dayCanComplete[task] = day + space + 1
        
        return day