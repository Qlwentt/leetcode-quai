class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # [1,2,3,4,5,6,7,8,9,10]
        #                    L
        #                    R        
        def canShip(capacity):
            daysTaken = 1
            L = 0
            curSum = 0
            for R in range(len(weights)):
                if weights[R] > capacity:
                    return False
                curSum += weights[R]
                if curSum > capacity:
                    L = R
                    curSum = weights[R]
                    daysTaken += 1
                if daysTaken > days:
                    return False
            return True
                
        lo = max(weights)
        hi = sum(weights)
        
        while lo <= hi:
            mid = (lo+hi) // 2
            
            if canShip(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
        