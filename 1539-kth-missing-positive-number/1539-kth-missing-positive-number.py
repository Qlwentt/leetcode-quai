class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        L = 0
        R = len(arr) - 1
        
        while L <= R:
            mid = (L+R) // 2
            
            missingToLeft = arr[mid] - (mid+1)
            if missingToLeft >= k:
                R = mid - 1
            else:
                L = mid + 1
                
        return L + k
        