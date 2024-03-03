from sortedcontainers import SortedSet
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedSet()
        
        L = 0
        answer = []
        for R in range(len(nums)):
            window.add((nums[R], R))
            
            while R - L + 1 > k:
                window.remove((nums[L], L))
                L += 1
            if R - L + 1 == k:
                median = window[len(window) // 2][0] if len(window) % 2 else (window[len(window) // 2][0] + window[len(window) // 2 -1][0]) / 2
                answer.append(median)
        
        return answer
            
        