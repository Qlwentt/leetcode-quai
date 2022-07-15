class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i, point in enumerate(points):
            x, y = point
            distance = math.sqrt(((x-0)**2) + (y - 0)**2)
            distances.append((distance,i))
        heapq.heapify(distances)
        i = 0
        answer = []
        while i < k:
            answer.append(points[heapq.heappop(distances)[1]])
            i += 1
        return answer
       