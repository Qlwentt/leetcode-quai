class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = [0] * len(prices)
        
        for i in range(len(prices)):
            first_discount = 0
            for j in range(i+1, len(prices)):
                if first_discount:
                    continue
                if prices[j] <= prices[i]:
                    first_discount = prices[j]
            answer[i] = prices[i] - first_discount
        return answer