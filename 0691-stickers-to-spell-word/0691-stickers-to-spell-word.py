from collections import Counter
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickersCounters = []
        for s in stickers:
            stickersCounters.append(Counter(s))
        memo = {}
        
        def dfs(curSticker, target):
            if target in memo:
                return memo[target]
            
            result = 1 if curSticker else 0
            remainder = ""
            
            for char in target:
                if char in curSticker and curSticker[char] > 0:
                    curSticker[char] -= 1
                else:
                    remainder += char
                    
            if remainder:
                used = float('inf')
                for newSticker in stickersCounters:
                    if remainder[0] in newSticker:
                        used = min(dfs(newSticker.copy(), remainder), used)
                memo[remainder] = used
                result += used
            return result
        answer = dfs({}, target)
        return answer if answer != float('inf') else -1
            