class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        maxPens, maxPencils = total // cost1, total // cost2
        answer = 0
        for i in range(maxPens+1):
            leftOver = total - (cost1*i)
            answer += (leftOver // cost2) + 1
        return answer