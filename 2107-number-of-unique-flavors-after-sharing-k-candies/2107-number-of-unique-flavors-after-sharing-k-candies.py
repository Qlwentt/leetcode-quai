class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        flavors = collections.Counter(candies)
        if k == 0:
            return len(flavors)
        answer = 0
        l = 0
        for r in range(len(candies)):
            flavors[candies[r]] -= 1
            if flavors[candies[r]] == 0:
                del flavors[candies[r]]
            if r-l+1 == k:
                answer = max(len(flavors), answer)
                flavors[candies[l]] += 1
                l += 1
        return answer
                
        
        