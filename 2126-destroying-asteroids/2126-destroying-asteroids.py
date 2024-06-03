from sortedcontainers import SortedList
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort(reverse=True)
        while asteroids:
            if mass >= asteroids[-1]:
                mass += asteroids.pop()
            else:
                return False
        return True