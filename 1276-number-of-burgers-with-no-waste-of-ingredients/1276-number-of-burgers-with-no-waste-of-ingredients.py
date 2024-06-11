class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # 4*1 = 4
        # 2*6 = 12
        lo = 0
        hi = cheeseSlices
        
        while lo <= hi:
            mid = (lo+hi) // 2
            
            jumbo = mid
            small = cheeseSlices - mid
            curTomato = jumbo * 4 + small * 2
            if curTomato == tomatoSlices:
                return [jumbo, small]
            if curTomato > tomatoSlices:
                hi = mid - 1
            else:
                lo = mid + 1
        return []
        
        