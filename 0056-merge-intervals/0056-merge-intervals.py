class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        answer = [intervals[0]]
        
        for start, end in intervals[1:]:
            prevStart, prevEnd = answer[-1]
            if start <= prevEnd:
                ansStart = min(start, prevStart)
                ansEnd = max(end, prevEnd)
                answer[-1] = [ansStart, ansEnd]
            else:
                answer.append([start, end])
                
        return answer