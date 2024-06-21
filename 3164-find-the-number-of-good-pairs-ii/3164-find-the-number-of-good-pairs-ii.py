class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def getFactors(n): 
            factors = set()
            for i in range(1,int(math.sqrt(n))+1):
                if n % i == 0:
                    factors.add(i)
                    factors.add(n // i)
            return factors
        counts2 = collections.Counter([num2*k for num2 in nums2])        
        
        # [2,9,2,4,8,3]
        #  P
        # [2,1,2,4,8,3,6,5]
        #  Q
        answer = 0
        for a in nums1:
            factors = getFactors(a)
            for factor in factors:
                answer += counts2[factor]
        
        return answer
            
        
        