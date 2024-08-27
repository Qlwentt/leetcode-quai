class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
                
        prefix_sums = {-1: 0}
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            prefix_sums[i] = cur_sum
        
        complements = {}
        max_sum = float('-inf')
        for i, num in enumerate(nums):
            
            if num - k in complements:
                j = complements[num-k]
                max_sum = max(prefix_sums[i] - prefix_sums[j-1], max_sum)
            if num + k in complements:
                j = complements[num+k]
                max_sum = max(prefix_sums[i] - prefix_sums[j-1], max_sum)
                
            if num not in complements:
                complements[num] = i
            else:
                old = prefix_sums[i] - prefix_sums[complements[num]-1]
                
                if old < num:
                    complements[num] = i
        
        return max_sum if max_sum != float('-inf') else 0
