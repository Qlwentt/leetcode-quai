class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        
        stack = [] # (val, index)
        
        for r, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                lesser_temp, l = stack.pop()
                answer[l] = r-l
            stack.append((temp, r))
            
        return answer
    
# Time: O(N)
# Space: O(N)