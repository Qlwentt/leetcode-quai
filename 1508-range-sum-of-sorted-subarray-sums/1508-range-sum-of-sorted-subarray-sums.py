class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefix_sums = [0]*len(nums)
        #[0,1,3,6,10]
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            prefix_sums[i] = cur_sum
        prefix_sums.insert(0,0)
        print(prefix_sums)
        sub_array_sums = []
        
        for i in range(1,len(prefix_sums)):
            for j in range(i):
                sub_array_sums.append(prefix_sums[i]-prefix_sums[j])
        sub_array_sums.sort()
        
        answer = 0
        for i in range(left-1, right):
            answer += sub_array_sums[i]
        
        return answer % (10**9+7)
        
         