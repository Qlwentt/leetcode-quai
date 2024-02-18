class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
       # [2,3,4,7,11] 7 - (3 + 1) 11 - (4 +1)
       #  1 1 1 3 6
            
       # [1,2,3,4]
       #  0 0 0 0
        
        
    #  [1,7,11,14,29,31,40,44]
    #   0 
        L = 0
        R = len(arr) - 1
        
        while L <= R:
            mid = (L+R) // 2
            
            if arr[mid] - (mid +1) >= k:
                R = mid - 1
            else:
                L = mid + 1
                
        return L + k
        
        
        