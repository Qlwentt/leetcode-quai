class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = [0] + spaces + [len(s)]
        answer = []
        for i in range(1, len(spaces)):
            answer.append(s[spaces[i-1]:spaces[i]])
        
        return " ".join(answer)
            
        
        
        
        