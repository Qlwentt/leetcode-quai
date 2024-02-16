class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        answer = [0]*n
        for log in logs:
            id_, command, time = log.split(":")
            time = int(time)
            id_ = int(id_)
            
            if command == "start":
                stack.append((id_,time))
            else:
                sId , start = stack.pop()
                end = time
                duration = end - start + 1
                answer[sId] += duration
                if stack:
                    prevId, time = stack[-1]
                    answer[prevId] -= duration
        return answer