class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        drank = 0
        while full != 0 or empty - numExchange >= 0:
            drank += full # 10
            empty += full# 10, 7, 3
            full = 0 # 0, 1, 2
            while empty - numExchange >= 0: # numEx: 3,4,5
                # print(empty, full, numExchange)
                empty -= numExchange
                full += 1
                numExchange += 1
                # print(empty, full, numExchange)
        return drank