from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = defaultdict(list)
        
        for course , prereq in prerequisites:
            prereqMap[course].append(prereq)
        
        visiting = set()
            
        def canTakeCourse(course):
            if course in visiting:
                return False
            if prereqMap[course] == []:
                return True
            visiting.add(course)
            for prereq in prereqMap[course]:
                if not canTakeCourse(prereq):
                    return False
            visiting.remove(course)
            prereqMap[course] = []
            return True
        
        for i in range(numCourses):
            if not canTakeCourse(i):
                return False
        return True