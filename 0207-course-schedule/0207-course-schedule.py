class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            adjList[course].append(pre)
        visited = set()
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            
            for neigh in adjList[course]:
                if not dfs(neigh):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True