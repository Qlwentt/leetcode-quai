class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        
        answer = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            prevStart, prevEnd = answer[-1]
            # need to merge
            if prevEnd >= start:
                new = [min(prevStart, start),max(prevEnd, end)]
                answer[-1] = new
            else:
                answer.append([start, end])
        return answer