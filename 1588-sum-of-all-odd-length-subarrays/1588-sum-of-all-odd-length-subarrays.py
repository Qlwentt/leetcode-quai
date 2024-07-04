class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # [1,4,2,5,3]
        # [0,1,5,7,12,15]  
        #    I
        #      J
        prefix_sums = [0] * len(arr)
        cur_sum = 0
        
        for i, num in enumerate(arr):
            cur_sum += num
            prefix_sums[i] += cur_sum
        prefix_sums.insert(0,0)
        
        answer = 0
        for i in range(len(prefix_sums)):
            for j in range(i+1, len(prefix_sums)):
                if (j - i) % 2 == 1:
                    answer += prefix_sums[j] - prefix_sums[i]
        return answer