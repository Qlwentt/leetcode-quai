class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        queens = set([tuple(queen) for queen in queens])
        
        answer = []
        # up
        r, c = king
        while r in range(8):
            if (r,c) in queens:
                answer.append([r,c])
                break
            r -= 1
        # down
        r, c = king
        while r in range(8):
            if (r,c) in queens:
                answer.append([r,c])
                break
            r += 1
            
        # left
        r, c = king
        while c in range(8):
            if (r,c) in queens:
                answer.append([r,c])
                break
            c -= 1
    
        r, c = king   
        while c in range(8):
            if (r,c) in queens:
                answer.append([r,c])
                break
            c += 1
        
        r, c = king
        while r in range(8) and c in range(8):
            if (r,c) in queens:
                answer.append([r,c])
                break
            r += 1
            c += 1
            
        r, c = king
        while r in range(8) and c in range(8):
            if (r,c) in queens:
                answer.append([r,c])
                break
            r -= 1
            c -= 1
            
        r, c = king
        while r in range(8) and c in range(8):
            if (r,c) in queens:
                answer.append([r,c])
                break
            r += 1
            c -= 1
        
        r, c = king
        while r in range(8) and c in range(8):
            if (r,c) in queens:
                answer.append([r,c])
                break
            r -= 1
            c += 1
        
        return answer
        
        
            
        