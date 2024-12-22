class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        answer = [-1] * len(queries)
        groups = defaultdict(list)
        
        for i, (l, r) in enumerate(queries):
            l, r = sorted([l,r])
            if l == r or heights[r] > heights[l]:
                answer[i] = r
            else:
                groups[r].append( (max(heights[l], heights[r]), i))
        min_heap = []
        for i, h in enumerate(heights):
            for q_h, q_i in groups[i]:
                heapq.heappush(min_heap, (q_h, q_i))
            while min_heap and h > min_heap[0][0]:
                q_h, q_i = heapq.heappop(min_heap)
                answer[q_i] = i
        return answer
            
                
        