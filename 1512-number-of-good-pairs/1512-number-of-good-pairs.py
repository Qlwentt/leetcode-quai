class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        good = 0
        for num in nums:
            good += counts[num]
            counts[num] += 1
        return good
        
#         # 1,2,3,4,5 
#           0,1,3,6,10
            
#         1,2,3
#         12 13
#         23
