class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.append(0)
        banned.append(n+1)
        banned.sort()
        
        i = bisect.bisect_left(banned, n+1)
        banned = banned[:i+1]
        
        choices = []
        for x,y in zip(banned, banned[1:]):
            choices.extend(list(range(x+1,y)))
            
        
        lo = 0
        hi = len(choices) - 1
        
        while lo <= hi:
            mid = (lo+hi) // 2
            if sum(choices[:mid+1]) > maxSum:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi + 1
        
        # 2,3,4
        # 2 5 9  
        # l 
        #     r
        # print(hi)
        # return lo + 1
        
        # (5-1)-1
        # 2,3,4
        # 1,2,3,4,5,6,7,8,9,10
        