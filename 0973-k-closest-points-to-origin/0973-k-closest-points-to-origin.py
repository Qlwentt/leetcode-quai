class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt((points[i][0]-0)**2 +(points[i][1]-0)**2), i) for i in range(len(points))]
        heapq.heapify(distances)
        
        answer = []
        while k:
            answer.append(points[heapq.heappop(distances)[1]])
            k -= 1
            
        return answer