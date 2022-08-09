from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            first = minHeap[0]
            
            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
        
            
        
       
                
        
        
        