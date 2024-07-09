class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = collections.defaultdict(int)
        
        for i, num in enumerate(edges):
            scores[num] += i
        
        max_score = max(scores.values())
        for edge in range(len(edges)):
            if scores[edge] == max_score:
                return edge
        