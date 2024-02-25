class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            adjList[course].append(pre)
            
        answer = []
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
            
            visited.add(course)
            visiting.remove(course)
            answer.append(course)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return answer
        