class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 0
        dayToComplete = defaultdict(int)
        for task in tasks:
            day += 1
            if dayToComplete[task] > day:
                day = dayToComplete[task]
            dayToComplete[task] = day + space + 1
        return day
            
        