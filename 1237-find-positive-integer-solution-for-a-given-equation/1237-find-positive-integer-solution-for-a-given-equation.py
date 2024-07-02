"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:                 
        answers = []                 
        for x in range(1,1001):
            lo = 1
            hi = 1000
            
            while lo <= hi:
                y = (lo+hi) // 2
                
                potential_z = customfunction.f(x,y)
                if potential_z > z:
                    hi = y - 1
                elif potential_z < z:
                    lo = y + 1
                else:
                    answers.append([x,y])
                    break
        return answers
                        
        
                                    
                