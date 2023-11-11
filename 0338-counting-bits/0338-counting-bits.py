class Solution:
    def countBits(self, n: int) -> List[int]:
        def getBits(n):
            count = 0
            while n:
                if n & 1:
                    count += 1
                n = n >> 1
            return count
        
        answer = []
        for i in range(n+1):
            answer.append(getBits(i))
            
        return answer
    
            