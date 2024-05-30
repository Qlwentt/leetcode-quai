class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        losers = collections.defaultdict(int)
        lost_1 = []
        not_lost = []
        
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losers[loser] += 1
        
        for p in players:
            if p not in losers:
                not_lost.append(p)
            else:
                if losers[p] == 1:
                    lost_1.append(p)
                    
        return [sorted(not_lost), sorted(lost_1)]
            
    
            
        
        