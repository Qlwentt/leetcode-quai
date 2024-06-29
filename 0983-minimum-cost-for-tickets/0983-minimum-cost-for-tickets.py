class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(i):
            if i == len(days):
                return 0
            
            # Option 1: Buy a 1-day pass
            one_day_pass = costs[0] + dp(i + 1)
            
            # Option 2: Buy a 7-day pass
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1
            seven_day_pass = costs[1] + dp(j)
            
            # Option 3: Buy a 30-day pass
            j = i
            while j < len(days) and days[j] < days[i] + 30:
                j += 1
            thirty_day_pass = costs[2] + dp(j)
            
            return min(one_day_pass, seven_day_pass, thirty_day_pass)
        
        return dp(0)

            
            