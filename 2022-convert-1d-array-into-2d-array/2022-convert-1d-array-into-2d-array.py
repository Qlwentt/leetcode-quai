class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        answer = [[0] * n for i in range(m)]
        original = deque(original)
        for r in range(m):
            for c in range(n):
                if original:
                    answer[r][c] = original.popleft()
                else:
                    return []
        
        return answer if len(original) == 0 else []
        