class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() 
        answer = [intervals[0]]
        for start, end in intervals[1:]:
            if answer[-1][1] >= start: # overlap
                answer[-1] = [min(start, answer[-1][0]), max(end, answer[-1][1])]
            else:
                answer.append([start,end])
            
        
        return answer
    
# Time: O(N*log(N)) because you had to sort
# Space: O(N) for answer