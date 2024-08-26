from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_dict = defaultdict(int)
        prefix_dict[0] = 1
        
        cur_sum = 0
        answer = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in prefix_dict:
                answer += prefix_dict[cur_sum-k]
            prefix_dict[cur_sum] += 1
        
        return answer
    
# Time: O(N)
# Space: O(N)