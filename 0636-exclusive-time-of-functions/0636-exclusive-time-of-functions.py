class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        answer = [0] * n
        
        for log in logs:
            id_, command, time = log.split(":")
            id_ = int(id_)
            time = int(time)
            if command == "start":
                stack.append((id_, time))
                
            else:
                startI, start = stack.pop()
                end = time
                exTime = end - start + 1
                answer[id_] += exTime
                if stack:
                    prevId, prevTime = stack[-1]
                    answer[prevId] -= exTime
            
        return answer

# Time: O(N)
# Space: O(N)