class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        exclusiveTimes = [0] * n
        
        for log in logs:
            id_,command, time = log.split(":")
            id_ = int(id_)
            time = int(time)
            if command == "start":
                stack.append((id_, time))
            else:
                end = time
                startId, start = stack.pop()
                delta = end - start + 1
                exclusiveTimes[startId] += delta
                if stack:
                    prevId = stack[-1][0]
                    exclusiveTimes[prevId] -= delta
        return exclusiveTimes