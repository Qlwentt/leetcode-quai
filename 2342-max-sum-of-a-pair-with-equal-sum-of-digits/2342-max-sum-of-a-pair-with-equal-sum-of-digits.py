class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort()
        def sumDigits(num):
            answer = 0
            while num:
                answer += num % 10
                num = num // 10
            return answer
        
        sums = defaultdict(list)
        for num in nums:
            sums[sumDigits(num)].append(num)
       
        maxSum = float('-inf')
        for key, numsWithSum in sums.items():
            if len(numsWithSum) > 1:
                maxSum = max(numsWithSum[-1] + numsWithSum[-2], maxSum)
            
        return maxSum if maxSum != float('-inf') else  -1
            
        
            
        