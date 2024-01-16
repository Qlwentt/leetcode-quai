class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        
        prev = self.generate(numRows-1)
        lastPrev = prev[-1]
        new = []
        new.append(1)
        
        for i in range(len(lastPrev)):
            if i+1 in range(len(lastPrev)):
                new.append(lastPrev[i]+lastPrev[i+1])
        
        new.append(1)
        
        prev.append(new)
        return prev