class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        exclusiveTimes = [0] * n
        for log in logs:
            id_, command, timestamp = log.split(":")
            id_ = int(id_)
            timestamp = int(timestamp)
            if command == "start":
                stack.append((id_,timestamp))
            else:
                end = timestamp
                startId, start = stack.pop()
                
                delta = end - start + 1
                exclusiveTimes[startId] += delta
                if stack:
                    prevId = stack[-1][0]
                    exclusiveTimes[prevId] -= delta
        return exclusiveTimes