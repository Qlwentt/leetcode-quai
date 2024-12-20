class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        max_heap = [(-1, start_node)]
        visited = set() 
        adj_list = collections.defaultdict(list)
        
        for i, (n1, n2) in enumerate(edges):
            adj_list[n1].append((n2, succProb[i]))
            adj_list[n2].append((n1, succProb[i]))
            
        
        while max_heap:
            cur_weight, node = heapq.heappop(max_heap)
            if node in visited:
                continue
            if node == end_node:
                return cur_weight * -1
            visited.add(node)
            
            for neigh, weight in adj_list[node]:
                heapq.heappush(max_heap, (weight*cur_weight, neigh))
                    
        return 0
                    
                    
            
            