class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*(len(temperatures))
        stack = []
        
        for R, curTemp in enumerate(temperatures):
            while stack and curTemp > stack[-1][0]:
                lowerTemp, L = stack.pop()
                answer[L] = R - L
            stack.append((curTemp,R))
        return answer