from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionsAndSpeeds = [[p,s] for p,s in zip(position, speed)]
        stack = []

        for pos, speed in sorted(positionsAndSpeeds)[::-1]:
            timeArrived = (target - pos) / speed
            if not stack or timeArrived > stack[-1]:
                stack.append(timeArrived)
            
        return len(stack)

# O(n) time
# O(n) space