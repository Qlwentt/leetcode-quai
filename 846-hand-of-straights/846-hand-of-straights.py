class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        heapq.heapify(hand)
        
        groups = []
        group = []
        while True:
            if len(group) == groupSize:
                groups.append(group.copy())
                group = []
            if not hand:
                break
            card = heapq.heappop(hand)
            prevCard = group[-1] if group else card - 1
            saveCards = []
            while prevCard != (card -1) :
                if hand:
                    saveCards.append(card)
                    card = heapq.heappop(hand)
                else:
                    return False
            group.append(card)
            while saveCards:
                heapq.heappush(hand,saveCards.pop())
            
        
        return len(group) == 0
            
        
       
                
        
        
        