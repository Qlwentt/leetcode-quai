class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = [intervals[0]]
        
        for start, end in intervals[1:]:
            prevStart, prevEnd = answer[-1]
            if start <= prevEnd: # need to merge
                newStart = min(start, prevStart)
                newEnd = max(end, prevEnd)
                answer[-1] = [newStart, newEnd]
            else:
                answer.append([start, end])
                
        return answer