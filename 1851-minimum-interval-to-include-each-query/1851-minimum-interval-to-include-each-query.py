class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort()
        
        minHeap = []
        result = {}
        i = 0
        
        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            
            result[query] = minHeap[0][0] if minHeap else -1
        
        return [ result[q] for q in queries]