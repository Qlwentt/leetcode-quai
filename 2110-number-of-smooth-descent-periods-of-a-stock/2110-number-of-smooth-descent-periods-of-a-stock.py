class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        L = 0
        answer = 0
        for R in range(len(prices)):
            if R != 0 and prices[R] != prices[R-1]-1:
                L = R
            answer += R-L+1
        return answer