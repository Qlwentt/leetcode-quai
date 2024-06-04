class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        complements = collections.defaultdict(int) 
          
        for num in nums:
            if complements[k-num]:
                complements[k-num] -= 1
                count += 1
            else:
                complements[num] += 1 
        
        return count