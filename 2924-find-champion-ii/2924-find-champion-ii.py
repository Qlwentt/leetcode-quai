class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        stronger = set([i for i in range(n)])
        
        for strong, weak in edges:
            stronger.discard(weak)
            
        return list(stronger)[-1] if len(stronger) == 1 else -1