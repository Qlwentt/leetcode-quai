class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [ (math.sqrt((x1-0)**2 + (y1-0)**2),x1,y1) for x1, y1 in points]
        heapq.heapify(distances)
        answer = []
        while k:
            distance, x, y = heapq.heappop(distances)
            answer.append([x,y])
            k -= 1
            
        return answer