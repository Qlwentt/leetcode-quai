class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = sorted([(p,s) for p,s in zip(position, speed)]) 
        #[(0, 1), (3, 3), (5, 1), (8, 4), (10, 2)]
        # [12,7,1]
         #   12     3
        stack = []
        for p, s in data:
            arrive_time = (target - p) / s
            while stack and stack[-1] <= arrive_time: 
                stack.pop()
            stack.append(arrive_time)
        return len(stack)
        
        
        
        # 3 miles/hr, start mile 3     1 miles/hr start mile 5
        # 
        # mile 4  - 1/3 hr              mile 6  - 1 hr
        # mile 5  - 2/3 hr
        # mile 6  - 1 hr 
        
       
        