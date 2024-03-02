class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def findClosest(target):
            L = 0
            R = len(arr) - 1
            
            while L <= R:
                mid = (L+R) // 2
                
                if arr[mid] >= target:
                    R = mid - 1
                else:
                    L = mid + 1
            return L
        
        i = findClosest(x)
        
        L = i - 1
        R = i 
        
        while R - L - 1 < k:
            left = arr[L] if L >= 0 else float('inf')
            right = arr[R] if R < len(arr) else float('inf')
            if abs(right - x) < abs(left-x):
                R += 1
            else:
                L -= 1
            
            
        return arr[L+1:R]