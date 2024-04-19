class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        L = 0
        R = len(arr) - k
        
        while L <= R:
            mid = (L+R) // 2
            
            if (mid +k not in range(len(arr)) or 
                x - arr[mid] <= arr[mid+k] - x): # mid is closer, so R is too high
                R = mid - 1
            else:
                L = mid + 1
        
        return arr[L:L+k]
                
            
        