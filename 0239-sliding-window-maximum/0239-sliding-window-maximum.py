from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # [1 ,3 ,-1,-3,5 ,3 ,6 ,7 ], k = 3
    #                 L   
    #                       R
    # [9,10,9,-7,-4,-8,2,-6] 5   
#      L                     
#      R
 #   fr[10] back [10,10,9,2]
#    [-7,-8,7,5,7,1,6,0] 4| 7 7
    #  L
    #         R
    #fr [] back
    # monotonically increasing queue
    
        L = 0
        R = 0
        q = deque()
        answer = []
        
        while R < len(nums):
            num = nums[R]
            while q and num > q[0]:
                q.popleft()
            q.appendleft(num)
            if R - L + 1 == k:
                answer.append(q[-1])
                prevNum = nums[L]
                if prevNum == q[-1]:
                    q.pop()
                L += 1
            R += 1
        return answer
            