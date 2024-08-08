class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque([])
        answer = []
        l = 0
        # [1,3,-1,-3,5,3,6,7] [3,-1,-3]
        #  L
        #       R
        for r in range(len(nums)):
            while q and q[-1][1] < nums[r]:
                q.pop()
            q.append([r,nums[r]])
            if r-l+1 > k:
                if q[0][0] == l:
                    q.popleft()
                l += 1
            if r-l+1 == k:
                answer.append(q[0][1])
        return answer
        