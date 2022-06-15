from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [] # (temp, i)
        
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prevTemp, prevI = stack.pop()
                answer[prevI] = i - prevI
            stack.append((temp,i))
        return answer

# O(n) time
# O(n) space