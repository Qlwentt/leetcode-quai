from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        answer = 0
        cache = {}
        for x in range(len(ages)-1, -1, -1):
            if ages[x] in cache:
                answer += cache[ages[x]]
                continue
            lo = 0
            hi = x - 1
            
            while lo <= hi:
                y = (lo + hi) // 2
                if ages[y] <= 0.5  * ages[x] + 7:
                    lo = y + 1
                else:
                    hi = y - 1
                    
            answer += x - lo
            cache[ages[x]] = x - lo
#             #[16,16]
#         #      L
              
#             lo = 0
#             hi = x - 1
            
#             while lo <= hi:
#                 y = (lo + hi) // 2
#                 if ages[y] > ages[x]: 
#                     hi = y - 1
#                 else:
#                     lo = y + 1
            
#             upperBound = lo
#             print(upperBound, lowerBound )
#             count = upperBound - lowerBound
#             answer += count if count >= 0 else 0
        return answer
            
            
            