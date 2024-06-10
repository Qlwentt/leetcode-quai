class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # (x−h)2+(y−k)2=r2 (h,k) = center of circle, r = radius
        answer = [0] * len(queries)
        i = 0
        for h,k,r in queries:
            count = 0
            rSquared = r ** 2
            for x,y in points:                
                if ((x-h)**2) + ((y-k) ** 2) <= rSquared:
                    count += 1
            answer[i] = count
            i += 1
        return answer
        
        