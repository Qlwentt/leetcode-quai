class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedLength = len(nums1) + len(nums2)
        half = mergedLength // 2

        A = nums1
        B = nums2
        if len(A) > len(B):
            A, B = B, A
        # always deal with the shorter one
        
        L = 0
        R = len(A) - 1
        while True:
            midA = (L+R) // 2
            midB =  half - midA - 2
                        
            eleA = A[midA] if midA >= 0 else float('-inf')
            nextA = A[midA + 1] if midA + 1 < len(A) else float('inf')
            eleB = B[midB] if midB >= 0 else float('-inf')
            nextB = B[midB + 1] if midB + 1 < len(B) else float('inf')
            
            if eleA <= nextB and eleB <= nextA:
                # found correct partition
                # odd length - one partition is greater than another
                if mergedLength % 2 == 1:
                    return min(nextA, nextB)
                else:
                    # even length - both partitions are equal
                    return (max(eleA,eleB) + min(nextA,nextB)) / 2
            if eleA > nextB:
                # remove elements from A
                R = midA - 1
            else:
                # add elements to A
                L = midA + 1
        
        # -inf[1,3] inf
        #      M
        # -inf [2,4] inf
        #       M
        [1,2,3,4]
        
        
