class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(capacity, days):
            curWeight = 0
            for R in range(len(weights)):
                if weights[R] > capacity:
                    return False
                curWeight += weights[R]
                while curWeight > capacity:
                    curWeight = weights[R]
                    days -= 1
            return days > 0
        
        lo = max(weights)
        hi = sum(weights)
        
        while lo <= hi:
            mid = (lo+hi) // 2
            
            if canShip(mid, days):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
        