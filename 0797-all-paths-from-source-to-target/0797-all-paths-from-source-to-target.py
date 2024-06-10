class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjList = graph
        answer = []
        def dfs(node, path):
            if node is None:
                return
            if node == len(graph) - 1:
                answer.append(path.copy())
                return
            
            
            for neigh in adjList[node]:
                path.append(neigh)
                dfs(neigh,path)
                path.pop()
        
        dfs(0,[0])
        return answer
            
        
        
        