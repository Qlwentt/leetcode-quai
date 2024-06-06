class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        drank = 0
        while full != 0 or empty - numExchange >= 0:
            drank += full
            empty += full
            full = 0 
            while empty - numExchange >= 0:
                empty -= numExchange
                full += 1
                numExchange += 1
        return drank