class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        # 1 1
        # 2 2
        # 3 2
        # 4 4
        # 5 4
        # 6 4
        # 7 4
        # 8 8
        offset = 1
        for i in range(1,n+1):
            if offset * 2 == i:
                offset = offset * 2
            dp[i] = 1 + dp[i-offset]
        return dp
            