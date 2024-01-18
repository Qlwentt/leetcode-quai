class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums1,nums2):
            p1 = 0
            p2 = 0
            answer = []
            while p1 < len(nums1) or p2 < len(nums2):
                item1 = nums1[p1] if p1 < len(nums1) else float('inf')
                item2 = nums2[p2] if p2 < len(nums2) else float('inf')
                
                if item1 <= item2:
                    answer.append(item1)
                    p1 += 1
                else:
                    answer.append(item2)
                    p2 += 1
            return answer
        
        def mergeSort(nums):
            if len(nums) == 1:
                return nums
            
            M = len(nums) // 2
            left = nums[:M]
            right = nums[M:]
            
            return merge(mergeSort(left), mergeSort(right))
        
        return mergeSort(nums)
        