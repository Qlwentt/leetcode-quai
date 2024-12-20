from collections import defaultdict
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
            if node == end_node:
                return cur_weight * -1
            visited.add(node)
            
            for neigh, weight in adj_list[node]:
                if neigh not in visited:
                    heapq.heappush(max_heap, (weight*cur_weight, neigh))
                    
        return 0

#         max_heap = [(-1, start_node)]
#         visited = defaultdict(lambda: float('inf'))
#         visited[start_node] = -1
#         adj_list = defaultdict(list)
        
#         for i, (node1, node2) in enumerate(edges):
#             adj_list[node1].append((node2, succProb[i]))
#             adj_list[node2].append((node1, succProb[i]))
        
#         while max_heap:
#             weight, node = heapq.heappop(max_heap)
            
#             for neigh, neigh_weight in adj_list[node]:
#                 total_weight = neigh_weight * weight
#                 if total_weight < visited[neigh]:
#                     heapq.heappush(max_heap, (total_weight, neigh))
#                     visited[neigh] = total_weight
#         answer = visited[end_node]            
#         return -answer if answer != float('inf') else 0
        
                    
                    
            
            