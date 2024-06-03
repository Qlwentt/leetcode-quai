class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        ROWS = len(s)
        COLS = max([len(row) for row in s])
        
        matrix = [[" "] * COLS for _ in range(ROWS) ]
        
        for r, word in enumerate(s):
            for c, char in enumerate(word):
                matrix[r][c] = char
        
        answer = []        
        for c in range(COLS):
            word = []
            for r in range(ROWS):
                word.append(matrix[r][c])
            for i in range(len(word)-1, -1,-1):
                if word[i] == " ":
                    word[i] = ""
                else:
                    break
            answer.append("".join(word))
        return answer
        # "TO 
        # "BE 
        # "OR
        # "NOT
        # "TO
        # "BE"