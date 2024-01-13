class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        minHeap = [(0,src,0)] # price , node, stops
        adjList = {i: [] for i in range(n)}
        
        for from_, to, price in flights:
            adjList[from_].append((to, price))
        visited = {}
        while minHeap:
            curPrice, node, stops = heapq.heappop(minHeap)
            
            if node == dst and stops-1 <= k:
                return curPrice
            
            if node in visited and visited[node] <= stops:
                continue
            visited[node] = stops
                   
            for neigh, price in adjList[node]:
                heapq.heappush(minHeap, (price+curPrice, neigh, stops+1))
        
        return -1
        
        