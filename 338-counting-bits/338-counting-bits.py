class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            result.append(self.count(i))
        return result
    
    def count(self,n):
        count = 0
        while n:
            if (n&1 == 1):
                count += 1
            n  =  n >> 1
        return count