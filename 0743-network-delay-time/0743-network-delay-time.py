class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i: [] for i in range(1,n+1)}
        
        for src, dst, w in times:
            adj_list[src].append((dst, w))
            
        min_heap = [(0, k)]
        visited = defaultdict(lambda: float('inf'))
        visited[k] = 0
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            for neigh, neigh_time in adj_list[node]:
                if neigh_time+time < visited[neigh]:
                    heapq.heappush(min_heap, (neigh_time+time, neigh))
                    visited[neigh] = neigh_time+time
            
        return max(visited.values()) if len(visited) == n else -1
 # Time O(Elog(E) + V)
# Space: O(E+V)
                
            