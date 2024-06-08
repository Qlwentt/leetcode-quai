
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        q = collections.deque([(skill, i, 0) for i, skill in enumerate(skills)])
        k = k % len(skills) + len(skills) if k > len(skills) else k
        while q:
            skill1, player1, wins1 = q.popleft()
            skill2, player2, wins2 = q.popleft()
            
            if wins1 == k:
                return player1
            
            if wins2 == k:
                return player2
            
            if skill1 > skill2:
                q.appendleft((skill1, player1, wins1+1))
                q.append((skill2,player2, 0))
            else:
                q.appendleft((skill2,player2, wins2+1))
                q.append((skill1,player1, 0))
                
        
        