class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curSum = 0 
        L = 0
        R = 0
        meets = 0
        size = 0
        
        while R < len(arr):
            size += 1
            curSum += arr[R]
            if size > k:
                size -= 1
                curSum -= arr[L]
                L += 1
            if size == k and (curSum /size) >= threshold:
                meets += 1
            R += 1
        return meets
            
            
        
        