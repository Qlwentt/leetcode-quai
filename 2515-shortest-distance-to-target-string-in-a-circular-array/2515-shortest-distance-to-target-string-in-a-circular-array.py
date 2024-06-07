class Solution:
    def closetTarget(self, words: List[str], target: str, start: int) -> int:
#         0,4       1
#         found, start
        
#         # left =  start - found % 5 
#         # right = found - start % 5
        answer = float('inf')
        for i, word in enumerate(words):
            if word == target:
                left = (start - i) % len(words)
                right = (i-start) % len(words)
                answer = min(answer, left, right)     
        
        return answer if answer != float('inf') else -1
        