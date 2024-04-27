class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        L = 0
        R = len(arr) - 1
        
        while L <= R:
            mid = (L+R) // 2
            
            if arr[mid] - (mid+1) >= k:
                R = mid - 1
            else:
                L = mid + 1
        # arr[R] - (R+1)
        # arr[R] - R - 1
        # arr[R] + k - (arr[R] - R - 1)
        # arr[R] +k -arr[R] + R + 1
        #k + R+1
        return k + R + 1