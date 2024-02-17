class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # [1,2,3,4,5,6,7,8,9,10]
        #                    L
        #                    R        
        def canShip(capacity):
            daysAvail = days
            L = 0
            curSum = 0
            for R in range(len(weights)):
                if weights[R] > capacity:
                    return False
                curSum += weights[R]
                if curSum > capacity:
                    L = R
                    curSum = weights[R]
                    daysAvail -= 1
            return daysAvail > 0
                
        lo = max(weights)
        hi = sum(weights)
        
        while lo <= hi:
            mid = (lo+hi) // 2
            
            if canShip(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
        