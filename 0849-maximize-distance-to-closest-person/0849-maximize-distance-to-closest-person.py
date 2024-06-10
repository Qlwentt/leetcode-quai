class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        count = 0
        answer = 0
        
        for seat in seats:
            if seat == 1:
                count = 0
            else:
                count += 1
                answer = max(answer, math.ceil(count/2))
        
        for i, seat in enumerate(seats):
            if seat == 1:
                answer = max(i, answer)
                break
        
        for i in range(len(seats)-1, -1,-1):
            if seats[i] == 1:
                answer = max(len(seats)-1-i, answer)
                break
                
        return answer
        
        