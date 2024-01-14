class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {i: [] for i in range(n)}
        minHeap = [(0,src, 0)] # price, node, stops
        
        for from_, to, price in flights:
            adjList[from_].append((to, price))
        cheapestPath = {i: (float(inf), float(inf)) for i in range(n)  } # price, stops 
        while minHeap:
            curPrice, node, stops = heapq.heappop(minHeap)
            
            if curPrice >= cheapestPath[node][0] and stops >= cheapestPath[node][1]:
                continue
            cheapestPath[node] = (curPrice, stops)
                        
            if node == dst and stops-1 <= k:
                return curPrice
            
            for neigh, neighPrice in adjList[node]:
                heapq.heappush(minHeap, (curPrice+neighPrice, neigh, stops+1))
        return -1
        