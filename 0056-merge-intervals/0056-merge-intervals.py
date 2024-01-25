class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0]) # sort by start
        answer = [intervals[0]]
        
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if prevEnd >= start: # overlap
                merged = [min(start, answer[-1][0]), max(end, prevEnd)]
                answer[-1] = merged
                prevEnd = max(end, prevEnd)
            else:
                answer.append([start,end])
                prevEnd = end
        
        return answer
    
# Time: O(N*log(N)) because you had to sort
# Space: O(N) for answer