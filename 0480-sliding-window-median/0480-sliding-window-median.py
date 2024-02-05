class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        L = 0
        answer = []
        window = []
        for R in range(len(nums)):
            bisect.insort(window, nums[R])
            while R - L + 1 > k:
                window.pop(bisect.bisect_left(window, nums[L]))
                L += 1
            if R - L + 1 == k: 
                median = (window[k // 2] + window[(k // 2) - 1]) / 2 if k % 2 == 0 else window[k// 2] 
                answer.append(median)
        
        return answer
        