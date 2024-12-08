class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        cache = {}
        events.sort()
        def dp(i, num_events):
            if num_events == 2 or i == len(events):
                return 0

            if (i, num_events) in cache:
                return cache[(i, num_events)]

            # choose
            curr_end = events[i][1]
            lo = i + 1
            hi = len(events) - 1
            next_event = None
            while lo <= hi:
                mid = (lo + hi) // 2
                if events[mid][0] > curr_end:
                    hi = mid - 1
                    next_event = mid
                else:
                    lo = mid + 1
            pick = float('-inf')
            if next_event != None:
                pick = events[i][2] + dp(next_event, num_events+1)
            else:
                pick = events[i][2]

            # skip 
            exclude = dp(i+1, num_events)

            ans = max(pick, exclude)
            cache[(i, num_events)] = ans
            return ans
        return dp(0,0)
            
        
        
        
        
        