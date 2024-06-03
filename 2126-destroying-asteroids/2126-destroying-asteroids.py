from sortedcontainers import SortedList
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = SortedList(asteroids)
        cur_mass = mass
        def get_best_asteroid(target):
            
            L = 0
            R = len(asteroids) -1
            
            while L <= R:
                mid = (L+R) // 2
                
                if asteroids[mid] > target:
                    R = mid - 1
                else:
                    L = mid + 1
            return R if R >= 0 else None
        
        while len(asteroids):
            # pick = get_best_asteroid(cur_mass)
            pick = asteroids.bisect_right(cur_mass) - 1
            if pick is -1:
                return False
            
            cur_mass += asteroids[pick]
            asteroids.pop(pick)
           
        
        return True
            
            