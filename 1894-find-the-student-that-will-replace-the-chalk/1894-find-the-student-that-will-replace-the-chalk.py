class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        
        for i in range(len(chalk)):
            k -= chalk[i]
            if k < 0:
                return i