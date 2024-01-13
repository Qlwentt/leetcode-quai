class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        maxHeap = [(-1, start_node)]
        maxPaths = {}
        adjList = {i:[] for i in range(n)}
        
        for i, (n1, n2) in enumerate(edges):
            adjList[n1].append((n2, succProb[i]))
            adjList[n2].append((n1, succProb[i]))
            
        
        while maxHeap:
            curWeight, node = heapq.heappop(maxHeap)
            if node in maxPaths:
                continue
            if node == end_node:
                return curWeight * -1
            maxPaths[node] = curWeight
            
            for neigh, weight in adjList[node]:
                if neigh not in maxPaths:
                    heapq.heappush(maxHeap, (weight*curWeight, neigh))
                    
            
                    
        return 0
                    
                    
            
            