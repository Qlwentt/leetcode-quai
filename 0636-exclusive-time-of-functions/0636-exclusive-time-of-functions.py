class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        answer = [0] * n
        for log in logs:
            id_, command, timestamp = log.split(":")
            id_ = int(id_)
            timestamp = int(timestamp)
            
            if command == "start":
                stack.append((id_, timestamp))
            else:
                end = timestamp
                start = stack.pop()[1]
                duration = end - start + 1
                answer[id_] += duration
                if stack:
                    prevId = stack[-1][0]
                    answer[prevId] -= duration
        return answer
        