class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       # is there a cycle in the graph
        adjList = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
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
        
        for course in range(numCourses):
            if not dfs(course):
                return False
    
        return True
            
                
        