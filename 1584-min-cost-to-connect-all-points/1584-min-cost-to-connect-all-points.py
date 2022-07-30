from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjList = defaultdict(list)
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1,n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append((distance, j))
                adjList[j].append((distance, i))
    
        totalCost = 0
        minHeap = [(0,0)]
        visited = set()
        
        while len(visited) < n:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            totalCost += cost
            
            visited.add(node)
            for neighCost, neigh in adjList[node]:
                if neigh not in visited:
                    heapq.heappush(minHeap, (neighCost, neigh))
        
        return totalCost