class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visited = set()
        visiting = set()
        
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)
            visited.add(node)
            
            for neigh in adjList[node]:
                if not dfs(neigh):
                    return False
            visiting.remove(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
        