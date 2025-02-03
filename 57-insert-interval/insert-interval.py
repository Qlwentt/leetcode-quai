class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       
        answer = []
        for i, (start, end) in enumerate(intervals):
            if newInterval[1] < start:
                answer.append(newInterval)
                return answer + intervals[i:]
            if newInterval[0] > end:
                answer.append(intervals[i])
            else:
                # merge
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
        answer.append(newInterval)
        return answer
    # Time: O(N)
    # Space: O(N)