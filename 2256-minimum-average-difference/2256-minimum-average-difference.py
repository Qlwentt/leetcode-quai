class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        [0, 2, 7, 10,19,24,27]
        [27,25,20,17,8, 3, 0]
        
        left = [0]
        right = collections.deque([0])
        
        cur_sum = 0
        for num in nums:
            cur_sum += num
            left.append(cur_sum)
        
        cur_sum = 0    
        for num in nums[::-1]:
            cur_sum += num
            right.appendleft(cur_sum)

        min_avg = float('inf')
        answer = None
        n = len(nums)
        for i in range(n):
            first = int(left[i+1] / (i+1))
            last = int(right[i+1] / (n - i -1)) if n - i - 1 else 0
            abs_diff = abs(first - last)
            if abs_diff < min_avg:
                min_avg = abs_diff
                answer = i
        return answer
            
            