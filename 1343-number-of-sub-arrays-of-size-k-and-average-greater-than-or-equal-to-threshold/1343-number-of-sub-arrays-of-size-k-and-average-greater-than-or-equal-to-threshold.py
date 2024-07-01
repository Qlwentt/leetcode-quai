class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        curSum = 0
        answer = 0
        for R in range(len(arr)):
            if R - L + 1 > k:
                curSum -= arr[L]
                L += 1
            curSum += arr[R]
            if R - L + 1 == k and curSum/k >= threshold:
                answer += 1
        
        return answer