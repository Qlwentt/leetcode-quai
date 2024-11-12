class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted([(q,i) for i, q in enumerate(queries)])
        answer = [0] * len(queries)
        
        max_beauty = 0
        i = 0
        
        for query, q in queries:
            while i < len(items) and items[i][0] <= query:
                max_beauty = max(max_beauty, items[i][1])
                i += 1
            answer[q] = max_beauty
            
        return answer
        
        
        