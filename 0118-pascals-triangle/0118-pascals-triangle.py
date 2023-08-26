class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            answer = self.generate(numRows-1)
            previous = answer[-1]
            new = []
            new.append(1)
            for i in range(len(previous)-1):
                new.append(previous[i] + previous[i+1])
            new.append(1)
            answer.append(new)
            
            return answer
       
        