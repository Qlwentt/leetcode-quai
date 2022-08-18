from math import sqrt
from heapq import heapify
from heapq import heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i, point in enumerate(points):
            x,y = point
            distance = sqrt((x - 0) ** 2 + (y - 0) ** 2)
            distances.append((distance, i))
        heapify(distances)

        answer = []
        i = 0
        while i < k:
            _, index = heappop(distances)
            answer.append(points[index])
            i += 1
        return answer
       