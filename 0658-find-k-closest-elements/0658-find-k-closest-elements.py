class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        def findClosest(target):
            lo = 0
            hi = len(arr) - 1
            
            while lo <= hi:
                mid = (lo + hi) // 2
                
                if  arr[mid] >= target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return lo
        i = findClosest(x)
        
        L = i - 1
        R = i
        
        while R - L - 1 < k:
            left = arr[L] if L in range(len(arr)) else float('inf')
            right = arr[R] if R in range(len(arr)) else float('inf')
         
            if abs(left-x) <= abs(right-x):
                L -= 1
            else: #abs(right-x) < abs(left-x):
                R += 1
            
        
        return arr[L+1:R]
                
                