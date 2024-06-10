class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        counts = {i:0 for i in range(n)}
        i = 0
        step = 1
        while counts[i] < 1:
            counts[i] += 1
            i = ( i+ step * k) % n 
            step += 1
                
        return [i+1 for i, count in counts.items() if count == 0]
        