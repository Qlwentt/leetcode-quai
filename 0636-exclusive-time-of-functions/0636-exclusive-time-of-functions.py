class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0]*n
        stack = []
        prevStart = 0
        
        for log in logs:
            funcId, command, time = log.split(":")
            
            funcId = int(funcId)
            time = int(time)
            
            if command == "start":
                if stack:
                    times[stack[-1]] += time - prevStart
                stack.append(funcId)
                prevStart = time
            else:
                
                end = time
                delta = end - prevStart + 1
                times[stack.pop()] +=  delta
                prevStart = end + 1
        return times