from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = max(piles)
        l = 1
        r = minK
        while l <= r:
            k = l + (r - l) // 2
            hoursToEat = 0
            for pile in piles:
                hoursToEat += ceil(pile/k)
            if hoursToEat <= h:
                # found a good k. try to find lower
                minK = min(minK,k)
                r = k - 1
            else:
                # hours too high, k too slow, try to find higher
                l = k + 1
        return minK
# O(log(max(piles)) * piles) time
# O(1) space