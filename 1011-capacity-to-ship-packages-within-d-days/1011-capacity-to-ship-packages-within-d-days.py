class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShipWithCapacity(capacity):
            curWeight = 0
            remainingDays = days
            for R in range(len(weights)):
                curWeight += weights[R]
                if weights[R] > capacity:
                    return False
                while curWeight > capacity:
                    curWeight = weights[R]
                    remainingDays -= 1
            
            return remainingDays > 0
        L = max(weights)
        R = sum(weights)
        
        while L <= R:
            mid = (L+R) // 2
            
            if canShipWithCapacity(mid): # look for lower
                R = mid - 1
            else:
                L = mid + 1
        return L
        
                    
            