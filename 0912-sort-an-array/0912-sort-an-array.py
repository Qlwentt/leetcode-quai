class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            answer = []
            L = 0
            R = 0
            
            while L < len(left) or R < len(right):
                Litem = left[L] if L < len(left) else float('inf')
                Ritem = right[R] if R < len(right) else float('inf')
                
                if Litem <= Ritem:
                    answer.append(Litem)
                    L += 1
                else:
                    answer.append(Ritem)
                    R += 1
            return answer
        
        
        def mergeSort(array):
            if len(array) == 1:
                return array
            
            M = len(array) // 2
            L = array[:M]
            R = array[M:]
            
            L = mergeSort(L)
            R = mergeSort(R)
            
            return merge(L,R)
        return mergeSort(nums)
            