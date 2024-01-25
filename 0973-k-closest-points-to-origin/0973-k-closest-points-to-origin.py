import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(math.sqrt((x1-0) ** 2 + (y1-0)**2), x1,y1) for x1,y1 in points]
        heapify(minHeap)
        
        answer = []
        
        while k:
            distance, x, y = heappop(minHeap)
            answer.append([x,y])
            k -= 1
            
        return answer