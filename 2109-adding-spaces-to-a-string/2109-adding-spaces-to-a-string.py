class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = [num + i for i,num in enumerate(spaces)]
        spaces.reverse()
        
        answer = [" "] * (len(s) + len(spaces))
        
        s = list(s)
        s.reverse()
        i = 0
        while s:
            if spaces and spaces[-1] == i:
                i += 1
                spaces.pop()
                continue
            answer[i] = s.pop()
            i += 1
        
        return "".join(answer)
            
        
        
        
        