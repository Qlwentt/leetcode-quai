class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = { course: [] for course in range(numCourses)}
        
        for course, pre in prerequisites:
            adjList[course].append(pre)
            
        order = []
        visited = set()
        visiting = set()
        
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visited.add(course)
            visiting.add(course)
            
            for neigh in adjList[course]:
                if not dfs(neigh):
                    return False
            
            order.append(course)
            visiting.remove(course)
            return True
        
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return order
    
# Time: O(M+N)
# Space: O(M+N)