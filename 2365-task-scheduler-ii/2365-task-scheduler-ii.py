from collections import defaultdict
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        waitTimes = defaultdict(int)
        day = 0
        for task in tasks:
            day = day + 1 if  waitTimes[task] <= day else waitTimes[task]
            waitTimes[task] = day + space + 1
        return day
            