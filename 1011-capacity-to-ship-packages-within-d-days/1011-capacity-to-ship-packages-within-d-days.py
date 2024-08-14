class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            days_taken = 1
            total_weight = 0
            for w in weights:
                if w > capacity:
                    return False
                total_weight += w
                if total_weight > capacity:
                    days_taken += 1
                    total_weight = w
            return days_taken <= days
        
        lo = max(weights)
        hi = sum(weights)
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if can_ship(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
    
# Time: O(Nlog(N))
# Space: O(1)
                