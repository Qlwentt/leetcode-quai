class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        count = len(asteroids)
        cur_mass = mass
        print(asteroids)
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
        
        while count:
            pick = get_best_asteroid(cur_mass)
            if pick is None:
                return False
            
            if cur_mass >= asteroids[pick]:
                cur_mass += asteroids[pick]
                asteroids.pop(pick)
                count -= 1
            else:
                return False
        
        return True
            
            