class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        leftDecreaseDays = [0] * n
        rightIncreaseDays = [0] * n

        for i in range(1, n):
            if security[i] <= security [i-1]:
                leftDecreaseDays[i] = leftDecreaseDays[i-1] + 1

        for i in range(n-2, -1, -1):
            if security[i] <= security [i+1]:
                rightIncreaseDays[i] = rightIncreaseDays[i+1] + 1

        answer = []
        for i in range(n):
            if leftDecreaseDays[i] >= time and  rightIncreaseDays[i] >= time:
                answer.append(i)

        return answer