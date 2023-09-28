from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = [(sandwich, 0) for sandwich in sandwiches]

        sandwiches.reverse()
        
        while students and sandwiches and sandwiches[-1][1] < len(students):
            student = students.popleft()
            if student == sandwiches[-1][0]:
                sandwiches.pop()
            else:
                sandwiches[-1] = (sandwiches[-1][0], sandwiches[-1][1] + 1)
                students.append(student)
        print(students)
        print(sandwiches)
        return len(students)