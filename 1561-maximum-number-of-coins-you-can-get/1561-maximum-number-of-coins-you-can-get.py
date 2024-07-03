class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        hi = len(piles) -1
        lo = 0
        coins = 0       
        while lo+1 < hi:
            lo += 1
            hi -= 1
            coins += piles[hi]
            hi -= 1
        return coins
        
        
        
        