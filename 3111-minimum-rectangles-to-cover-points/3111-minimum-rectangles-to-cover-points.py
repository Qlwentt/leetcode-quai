class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
#         min_heap = points
#         heapq.heapify(min_heap)
        
#         rectangles = []
#         while min_heap:
#             min_x, min_y = heapq.heappop(min_heap)
#             lower_x, upper_x, = rectangles[-1] if rectangles else [None, None]
#             if lower_x is None or min_x not in range(lower_x, upper_x+1):
#                 rectangles.append([min_x, min_x+w])
        
#         return len(rectangles)

            x_es = [x for x,y in points]
            x_es.sort()
            
            upper_x = -1 
            count = 0
            
            for x in x_es:
                if x > upper_x:
                    upper_x = x + w
                    count += 1
            return count
        
        