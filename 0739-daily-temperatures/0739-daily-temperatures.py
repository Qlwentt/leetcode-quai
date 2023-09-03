class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # [73,74,75,71,69,72,76,73]
        #  0  1. 2. 3. 4. 5. 6. 7
        # [1 , 1, 4, 2, 1, 1, 0, 0]
        #stack = [(76,6)(75,4)(74,1)(73,1)] 
        
        # [89,62,70,58,47,47,46,76,100,70]
        #   0  1  2  3  4  5  6  7  8  9
        # [0 , 0, 0, 0, 0, 2, 1, 1,  0, 0]
        #stack [(100,8),(76,7)(47)]
        #monotonically decreasing stack
        
        answer = [0] * len(temperatures)
        stack = [] # value, index
        
        for i in range(len(temperatures)-1,-1,-1):
            currentTemp = temperatures[i]
            while stack and currentTemp >= stack[-1][0]:
                stack.pop()
            if stack:
                answer[i] = stack[-1][1] - i
            stack.append((currentTemp, i))
        return answer