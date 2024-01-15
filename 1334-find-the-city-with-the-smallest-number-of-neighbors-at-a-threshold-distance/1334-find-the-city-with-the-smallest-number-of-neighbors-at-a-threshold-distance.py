class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjList = {i:[] for i in range(n)}
        
        for from_, to, weight in edges:
            adjList[from_].append((to, weight))
            adjList[to].append((from_, weight))
        
        def dijkstras(src):
            minHeap = [(0, src)]
            shortestPath = {i:float(inf) for i in range(n)}
            numCities = 0
            
            while minHeap:
                distance, node = heapq.heappop(minHeap)
                if distance >= shortestPath[node]:
                    continue
                shortestPath[node] = distance
                if distance <= distanceThreshold:
                    numCities += 1
                
                for neigh, neighDist in adjList[node]:
                    heapq.heappush(minHeap, (neighDist+distance, neigh))
            return numCities
        
        fewestCities = float(inf)
        answer = -1
        for i in range(n):
            numCities = dijkstras(i)
            fewestCities = min(fewestCities, numCities)
            if numCities == fewestCities:
                answer = i
        
        return answer
            
            