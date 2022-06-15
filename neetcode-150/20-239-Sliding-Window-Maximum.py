from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0:
            return []
        if k == 1:
            return nums
        
        start = 0
        end = 0
        answer = []
        
        deq = deque()

        while end < len(nums):
            while deq and deq[-1][1] < nums[end]:
                deq.pop()
            deq.append((end, nums[end]))
            windowSize = end - start + 1
                
            if windowSize == k:
                answer.append(deq[0][1])
                if start == deq[0][0]:
                    deq.popleft()
                start += 1
            
            end += 1   
        return answer