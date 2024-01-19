import math
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = {}
        for width, height in rectangles:
            ratio = width/height
            ratios[ratio] = 1 + ratios.get(ratio,0)
            
       # {0.5: 4} # number of combinations
        answer = 0
        for n in ratios.values():
            if n > 1:
                answer += comb(n,2)
            
        return answer
    
    # Completion Time: 09:16 min