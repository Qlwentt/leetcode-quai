from collections import Counter
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        availStickers = []
        for s in stickers:
            availStickers.append(Counter(s))
        memo = {}
        def dfs(curSticker, target):
            if target in memo:
                return memo[target]
            
            answer = 1 if curSticker else 0
            
            remainder = ""
            for char in target:
                if char in curSticker and curSticker[char] > 0:
                    curSticker[char] -= 1
                else:
                    remainder += char
            
            if remainder:
                used = float('inf')
                for newSticker in availStickers:
                    if remainder[0] in newSticker:
                        used = min(dfs(newSticker.copy(), remainder), used)
                memo[remainder] = used
                
                answer += used 
            return answer
        a = dfs({}, target)
        return a if a != float('inf') else -1
        