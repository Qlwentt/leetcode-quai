from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        canTake = set()
        visiting = set()
        prereqMap = defaultdict(list)
        order = []
        
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
            
        def canFinish(course):
            if course in canTake:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for prereq in prereqMap[course]:
                if not canFinish(prereq):
                    return False
            visiting.remove(course)
            canTake.add(course)
            order.append(course)
            return True
        
        for i in range(numCourses):
            if not canFinish(i):
                return []
        return order