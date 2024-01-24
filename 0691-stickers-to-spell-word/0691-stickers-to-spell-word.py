from collections import Counter
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickerCounters = []
        for sticker in stickers:
            stickerCounters.append(Counter(sticker))
        memo  = {} 
        def dfs(curSticker, t):
            if t in memo:
                return memo[t]
            res = 1 if curSticker else 0
            
            remainder = ""
            for char in t:
                if char in curSticker and curSticker[char] > 0:
                    curSticker[char] -= 1
                else:
                    remainder += char
            
            if remainder:
                used = float('inf')
                for newSticker in stickerCounters:
                    if remainder[0] in newSticker:
                        used = min(used,dfs(newSticker.copy(), remainder))
                memo[remainder] = used 
                res += used
           
                 
            return res
                        
            
        answer = dfs({}, target)
        
        
        return answer if answer != float('inf') else -1