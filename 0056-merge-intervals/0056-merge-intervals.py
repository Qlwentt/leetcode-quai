class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        
        answer = [intervals[0]]
        
        for start, end in intervals[1:]:
            if start <= answer[-1][1]: # need to merge
                newStart = min(start, answer[-1][0])
                newEnd = max(end, answer[-1][1])
                answer[-1] = [newStart, newEnd]
            else: # don't need to merge
                answer.append([start, end])
                
        return answer
                