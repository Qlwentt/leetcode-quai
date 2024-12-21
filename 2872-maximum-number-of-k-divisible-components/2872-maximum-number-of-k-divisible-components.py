class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        visited = set()
        adj_list = defaultdict(list)
        
        for parent, child in edges:
            adj_list[parent].append(child)
            adj_list[child].append(parent)
        
        result = 0 
        def dfs(node):
            nonlocal result
            
            visited.add(node)
            
            sum_ = values[node]
            for child in adj_list[node]:
                if child not in visited:
                    sum_ += dfs(child)
            
            if sum_ % k == 0:
                result += 1
            return sum_
                
        dfs(0)
        return result
        