class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i: [] for i in range(1,n+1)}
        
        for src, dst, w in times:
            adjList[src].append((dst, w))
            
        minHeap = []
        heapq.heappush(minHeap, (0, k))
        
        time = 0
        minTimes = {}
        while minHeap:
            curWeight, node = heapq.heappop(minHeap)
            if node in minTimes:
                continue
            minTimes[node] = curWeight
            time = max(time, curWeight)
            
            for neigh, neighWeight in adjList[node]:
                if neigh not in minTimes:
                    heapq.heappush(minHeap, (neighWeight+curWeight, neigh))
            
            
        return time if len(minTimes) == n else -1