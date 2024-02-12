from collections import Counter
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        availStickers = []
        for s in stickers:
            availStickers.append(Counter(s))
        
        memo = {}
        
        def dfs(curSticker, t):
            if t in memo:
                return memo[t]
            
            answer = 1 if curSticker else 0
            
            leftover = ""
            for char in t:
                if char in curSticker and curSticker[char] > 0:
                    curSticker[char] -= 1
                else:
                    leftover += char
            
            
            if leftover:
                used = float('inf')
                for newSticker in availStickers:
                    if leftover[0] in newSticker:
                        used = min(used, dfs(newSticker.copy(), leftover))
                memo[leftover] = used
                answer += used
            
            return answer
        
        a = dfs({}, target) 
        return a if a != float('inf') else -1