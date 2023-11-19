import re
from collections import defaultdict
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        exTime = [0] * n
        for log in logs:
            i, command, time = log.split(":")
            i = int(i)
            time = int(time)
            
            if command == "start":
                stack.append((i, time))
            else:
                startI, start = stack.pop()
                end = time
                xtime = end - start + 1
                exTime[startI] += xtime
                if stack:
                    j, start = stack[-1]
                    exTime[j] -= xtime
        return exTime