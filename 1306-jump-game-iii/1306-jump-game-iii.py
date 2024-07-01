class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        adjList = {i: [] for i in range(len(arr))}
        
        for i, num in enumerate(arr):
            right = i + num
            left = i - num
            if right in range(len(arr)):
                adjList[i].append(right)
            if left in range(len(arr)):
                adjList[i].append(left)
                
        visiting = set()
        def dfs(node):
            if arr[node] == 0:
                return True
            if node in visiting:
                return False
            
            visiting.add(node)
            for neigh in adjList[node]:
                if dfs(neigh):
                    return True
            visiting.remove(node)
            return False
        
        return dfs(start)
        