from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # can't have any cycle
        # all nodes must be connected
        adjList = defaultdict(list)
        
        for node, neigh in edges:
            adjList[node].append(neigh)
            adjList[neigh].append(node)
        
        visiting = set()
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return True
            if node in visiting:
                #there is a cycle
                return False 
            visiting.add(node)
            for neigh in adjList[node]:
                if parent == neigh:
                    continue
                if not dfs(neigh, node):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        if not dfs(0, None):
            return False
        return len(visited) == n