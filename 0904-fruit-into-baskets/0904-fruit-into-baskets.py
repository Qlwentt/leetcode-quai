class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
    
        basket = collections.defaultdict(int)
        L = 0
        max_length = 0
        for R in range(len(fruits)):
            basket[fruits[R]] += 1
            while len(basket) > 2:
                basket[fruits[L]] -= 1
                if basket[fruits[L]] == 0:
                    del basket[fruits[L]]
                L += 1
            max_length = max(R-L+1, max_length)
        return max_length
    
    # Time: O(N)
    # Space: O(1) (dictionary will be at most length 2 which is constant)