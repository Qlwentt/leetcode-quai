class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        cur_sum = 0
        L = 0
        points = 0
        for R in range(len(calories)):
            while R-L+1 > k:
                cur_sum -= calories[L]
                L += 1
            cur_sum += calories[R]
            if R - L + 1 == k:
                if cur_sum < lower:
                    points -= 1
                elif cur_sum > upper:
                    points += 1
            
        return points