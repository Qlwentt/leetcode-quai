from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        
        for node, neigh, weight in times:
            adjList[node].append((neigh, weight))
            
        
        minHeap = [(0, k)]
        visited = set()
        minTime = 0
        
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            minTime = max(weight, minTime)
            visited.add(node)
            
            for neigh, neighWeight in adjList[node]:
                heapq.heappush(minHeap,(neighWeight+weight, neigh))
        
        return minTime if len(visited) == n else -1
        