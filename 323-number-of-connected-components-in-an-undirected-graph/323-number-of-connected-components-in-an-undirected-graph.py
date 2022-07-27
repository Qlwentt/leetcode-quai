from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        
        for node, neigh in edges:
            adjList[node].append(neigh)
            adjList[neigh].append(node)
            
        visited = set()
        
        def isComponent(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in adjList[node]:
                if neigh != parent:
                    isComponent(neigh, node)
                    
            return True
        components = 0
        for i in range(n):
            if isComponent(i, None):
                components += 1
        
        return components