class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev = self.getRow(rowIndex-1)
        prev.append(0)
        answer = []
        for i in range(len(prev)):
            answer.append(prev[i-1]+ prev[i] if i-1 >= 0 else prev[i])
        return answer
    
        
        