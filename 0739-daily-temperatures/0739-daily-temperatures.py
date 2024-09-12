class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        
        stack = [] # (val, index)
        
        for end, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                lesser_temp, start = stack.pop()
                answer[start] = end-start
            stack.append((temp, end))
            
        return answer
    
# Time: O(N)
# Space: O(N)