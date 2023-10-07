from collections import deque
import copy

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {course: set() for course in range(numCourses)}
        fullPreMap = {course: set() for course in range(numCourses)}
        for pre, course in prerequisites:
            adjList[course].add(pre)
                
        visited = set()
        
        def dfs(course):
            if course in visited:
                return fullPreMap[course]
            visited.add(course)
            for neigh in adjList[course]:
                fullPreMap[course].add(neigh)
                fullPreMap[course].update(dfs(neigh))
            if not adjList[course]:
                return set([course])
            return fullPreMap[course]            
           
        for course in range(numCourses):
            dfs(course)
                    
        answers = []
        for pre, course in queries:
            answers.append(pre in fullPreMap[course])

        return answers