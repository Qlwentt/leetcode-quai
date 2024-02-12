from sortedcontainers import SortedSet
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        L = 0
        
        window = SortedSet() 
        
        answer = []
        for R in range(len(nums)):
            window.add((nums[R], R))
            
            while R - L + 1 > k:
                window.remove((nums[L], L))
                L += 1
            
            if R - L + 1 == k:
                median = window[k//2][0] if k % 2 else (window[k//2][0] + window[k//2 -1][0]) / 2
                answer.append(median)
        
        return answer

    # O( N log(k))
    # O(k)