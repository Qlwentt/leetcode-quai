from sortedcontainers import SortedSet
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        people = SortedSet([i for i in range(1,n+1)])
        i = 0
        while len(people) != 1:
            i = (i + k - 1) % len(people) 
            people.pop(i)
            
        return people[0]