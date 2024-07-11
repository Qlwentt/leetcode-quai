class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
    
        fruit_dict = collections.defaultdict(int)
        L = 0
        max_length = 0
        for R in range(len(fruits)):
            fruit_dict[fruits[R]] += 1
            while len(fruit_dict) > 2:
                fruit_dict[fruits[L]] -= 1
                if fruit_dict[fruits[L]] == 0:
                    del fruit_dict[fruits[L]]
                L += 1
            max_length = max(R-L+1, max_length)
        return max_length
    
    # Time: O(N)
    # Space: O(1) (dictionary will be at most length 2 which is constant)