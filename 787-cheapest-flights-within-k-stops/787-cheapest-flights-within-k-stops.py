from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        
        for i in range(k+1):
            tempPrices = prices[:]
            for frm, to, priceTo in flights:
                if prices[frm] == float(inf):
                    continue
                price = prices[frm] + priceTo
                if price < tempPrices[to]:
                    tempPrices[to] = price
            prices = tempPrices
            
        return prices[dst] if prices[dst] != float('inf') else -1
        