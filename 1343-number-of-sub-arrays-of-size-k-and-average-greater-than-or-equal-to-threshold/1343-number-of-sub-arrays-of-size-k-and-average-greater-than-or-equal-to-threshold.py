class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # [2,2,2,2,5,5,5,8]
        #    L
        #        R
        length = 0 # 1 2 3 4 3
        summ = 0 # 2 4 6 8 6
        L = 0
        R = 0
        answer = 0 # 
        # summ /k  6/3
        while R < len(arr):
            summ += arr[R]
            length += 1
            if length > k:
                summ -= arr[L]
                L += 1
                length -= 1
            if length == k and summ/k >= threshold:
                answer += 1
            R += 1
        return answer
            
            
        
        