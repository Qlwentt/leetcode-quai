class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posNSpeed = [(pos,spd) for pos, spd in zip(position,speed)]
        posNSpeed.sort(reverse=True)
        stack = [] # time to target
        for p, s in posNSpeed:
            time = (target-p)/s
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            
            
            
            
    