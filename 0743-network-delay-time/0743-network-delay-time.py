class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i:[] for i in range(1,n+1)}
        
        for src, dst, w in times:
            adjList[src].append((dst, w))
            
        
        minHeap = [(0, k)]
        minTime = -1
        times = {i:float(inf) for i in range(1,n+1)}
        while minHeap:
            time, node = heapq.heappop(minHeap)
            
            if time >= times[node]:
                continue
            times[node] = time
            minTime = max(time, minTime)
            
            for neigh, neighTime in adjList[node]:
                heapq.heappush(minHeap, (neighTime+time, neigh))
            
        return minTime if all(value != float(inf) for value in times.values()) else -1
            
                
            