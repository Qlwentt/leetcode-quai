class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(math.sqrt((x - 0)** 2 + (y-0)**2),x,y) for x,y in points]
        heapq.heapify(minHeap)
        answer = []
        while k:
            dist, x,y = heapq.heappop(minHeap)
            answer.append([x,y])
            k -= 1
        
        return answer