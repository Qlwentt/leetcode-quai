class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        answer = [0]* n
        
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
                answer[startId] += delta
                if stack:
                    prevId, prevtime = stack[-1]
                    answer[prevId] -= delta
        return answer