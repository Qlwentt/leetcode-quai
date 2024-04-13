from collections import Counter
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickerCounts = []
        for s in stickers:
            stickerCounts.append(Counter(s))
        memo = {}
        def backtrack(target, curSticker):
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
                minAnswer = float('inf')
                for newSticker in stickerCounts:
                    if remainder[0] in newSticker:
                        minAnswer = min(minAnswer, backtrack(remainder, newSticker.copy()))
                memo[remainder] = minAnswer
                result += minAnswer
                
            return result
        answer = backtrack(target, {})
        return answer if answer != float('inf') else -1 
            
            