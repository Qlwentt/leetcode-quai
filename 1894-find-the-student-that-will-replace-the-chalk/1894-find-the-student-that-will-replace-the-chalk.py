class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        
        for i, item in enumerate(chalk):
            k -= item
            if k < 0:
                return i
        return 0