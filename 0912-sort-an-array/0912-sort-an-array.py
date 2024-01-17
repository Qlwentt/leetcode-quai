class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums1, nums2):
            p1 = 0
            p2 = 0
            p3 = 0
            
            answer = [None] * (len(nums1) + len(nums2))
            
            while p1 in range(len(nums1)) or p2 in range(len(nums2)):
                item1 = nums1[p1] if p1 in range(len(nums1)) else float('inf')
                item2 = nums2[p2] if p2 in range(len(nums2)) else float('inf')
                
                if item1 <= item2:
                    answer[p3] = item1
                    p1 += 1
                else:
                    answer[p3] = item2
                    p2 += 1
                p3 += 1
            return answer
        
        def mergeSort(nums):
            if len(nums) == 1:
                return nums
            
            M = len(nums) // 2
            left = mergeSort(nums[:M])
            right = mergeSort(nums[M:])
            
            return merge(left,right)
            
            
        
        return mergeSort(nums)
            
        