class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        #{0:[1], 1:[2], 2:[3], 3:[4],}
        @cache
        def get_length(node, query_num):
            if node == n-1:
                return 0
            ans = float('inf')
            for neigh in adj_list[node]:
                 ans = min(1 + get_length(neigh,query_num), ans)
            return ans
        
        adj_list = {i: [i+1] for i in range(n)}
        answer = []
        i = 0
        for from_, to in queries:
            adj_list[from_].append(to)
            answer.append(get_length(0, i))
            i += 1
        return answer
        