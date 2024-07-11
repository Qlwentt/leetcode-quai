class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
    
        baskets = collections.defaultdict(int)
        L = 0
        max_length = 0
        for R in range(len(fruits)):
            baskets[fruits[R]] += 1
            while len(baskets) > 2:
                baskets[fruits[L]] -= 1
                if baskets[fruits[L]] == 0:
                    del baskets[fruits[L]]
                L += 1
            max_length = max(R-L+1, max_length)
        return max_length
    
    # Time: O(N)
    # Space: O(1) (dictionary will be at most length 2 which is constant)