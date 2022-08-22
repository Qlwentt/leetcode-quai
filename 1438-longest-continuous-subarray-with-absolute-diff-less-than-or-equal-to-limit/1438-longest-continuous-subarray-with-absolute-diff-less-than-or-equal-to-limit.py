from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decQ = deque([])
        incQ = deque([])
        
        l = 0
        longest = 0
        
        for r in range(len(nums)):
            num = nums[r]
            while decQ and nums[decQ[-1]] >= num:
                decQ.pop()
            
            while incQ and nums[incQ[-1]] <= num:
                incQ.pop()
            
            decQ.append(r)
            incQ.append(r)
            
            while decQ and incQ and abs(nums[decQ[0]] - nums[incQ[0]]) > limit:
                if decQ and decQ[0] == l:
                    decQ.popleft()
                if incQ and incQ[0] == l:
                    incQ.popleft()
                l+=1
            longest = max(longest, r-l+1)
        return longest
            
                