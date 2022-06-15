from typing import List
from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        
        count = {}
        for num in nums:
            itemCount = count.get(num, 0)
            count[num] = itemCount + 1
        
        return nlargest(k, count.keys(), key=count.get)
# O k log(n) time
# O(n+k) space

# alternative solution 
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counts = Counter(nums)
#         buckets = [ [] for i in range(len(nums) + 1)]
        
#         for ele, count in counts.items():
#             buckets[count].append(ele)
#         output = []
#         for i in range(len(buckets) -1, 0, -1):
#             bucket = buckets[i]
#             for num in bucket:
#                 output.append(num)
#                 if len(output) == k:
#                     return output
#
# O(n) time
# O(n) space